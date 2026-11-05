"""Summit QuickBooks pull, diff, and the unbilled join. The refresh token is saved when Intuit rotates it."""

import base64
import csv
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from nightshift.envfile import save_key

CHICAGO = ZoneInfo("America/Chicago")


def _refresh(env, path):
    basic = base64.b64encode(f"{env['QBO_CLIENT_ID']}:{env['QBO_CLIENT_SECRET']}".encode()).decode()
    form = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": env["QBO_REFRESH_TOKEN"],
    }).encode()
    request = urllib.request.Request(
        "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer",
        data=form,
        headers={
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        token = json.loads(response.read().decode())
    if token.get("refresh_token") and token["refresh_token"] != env.get("QBO_REFRESH_TOKEN"):
        save_key(path, "QBO_REFRESH_TOKEN", token["refresh_token"])
        env["QBO_REFRESH_TOKEN"] = token["refresh_token"]
    return token["access_token"]


def _query(access, realm, sql):
    url = (
        f"https://quickbooks.api.intuit.com/v3/company/{realm}/query?minorversion=75&query="
        + urllib.parse.quote(sql)
    )
    request = urllib.request.Request(url, headers={"Authorization": f"Bearer {access}", "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=40) as response:
        return json.loads(response.read().decode())


def _pages(access, realm, entity, where=""):
    rows = []
    start = 1
    while start < 4000:
        sql = f"SELECT * FROM {entity} {where} STARTPOSITION {start} MAXRESULTS 100"
        payload = _query(access, realm, sql)
        batch = (payload.get("QueryResponse") or {}).get(entity) or []
        rows.extend(batch)
        if len(batch) < 100:
            break
        start += 100
    return rows


def _customer_name(ref):
    if isinstance(ref, dict):
        return ref.get("name") or ""
    return ""


def pull(root, env, path, emailed_names):
    today = datetime.now(CHICAGO).date()
    marker = os.path.join(root, "state", "qbo-" + today.isoformat())
    os.makedirs(os.path.dirname(marker), exist_ok=True)
    if os.path.exists(marker):
        return None
    access = _refresh(env, path)
    realm = env["QBO_REALM_ID"]
    start = (today - timedelta(days=400)).isoformat()
    invoices = _pages(access, realm, "Invoice", f"WHERE TxnDate >= '{start}'")
    customers = _pages(access, realm, "Customer")
    directory = os.path.join(root, "artifacts")
    os.makedirs(directory, exist_ok=True)
    current = os.path.join(directory, "qbo-" + today.isoformat() + ".csv")
    with open(current, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Id", "TxnDate", "Customer", "TotalAmt", "DocNumber"])
        for invoice in invoices:
            writer.writerow([
                invoice.get("Id"),
                invoice.get("TxnDate"),
                _customer_name(invoice.get("CustomerRef")),
                invoice.get("TotalAmt"),
                invoice.get("DocNumber"),
            ])
    previous = _previous_ids(directory, today)
    current_ids = {str(invoice.get("Id")) for invoice in invoices}
    added = sorted(current_ids - previous)
    invoiced = {_customer_name(invoice.get("CustomerRef")).lower() for invoice in invoices}
    senders = [name.lower() for name in emailed_names if name]
    unbilled = []
    for customer in customers:
        name = (customer.get("DisplayName") or "").strip()
        if not name or name.lower() in invoiced:
            continue
        if any(name.lower() in sender or sender in name.lower() for sender in senders):
            unbilled.append(name)
    note_path = os.path.join(directory, "qbo-diff-" + today.isoformat() + ".json")
    payload = {
        "added_invoice_ids": added[:50],
        "invoice_count": len(invoices),
        "customer_count": len(customers),
        "unbilled": unbilled[:30],
    }
    with open(note_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    with open(marker, "w", encoding="utf-8") as handle:
        handle.write(str(len(invoices)))
    return payload


def _previous_ids(directory, today):
    names = sorted(
        name for name in os.listdir(directory)
        if name.startswith("qbo-") and name.endswith(".csv") and today.isoformat() not in name
    )
    if not names:
        return set()
    ids = set()
    with open(os.path.join(directory, names[-1]), encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("Id"):
                ids.add(row["Id"])
    return ids
