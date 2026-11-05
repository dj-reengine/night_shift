"""Google access tokens. Service accounts are signed with openssl. User tokens refresh in place."""

import json
import os
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request


def _post_form(url, form, headers=None):
    data = urllib.parse.urlencode(form).encode()
    request = urllib.request.Request(url, data=data, headers=headers or {}, method="POST")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode())


def _b64(raw):
    import base64
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def service_account_token(sa_path, scopes):
    with open(sa_path, encoding="utf-8") as handle:
        info = json.load(handle)
    now = int(time.time())
    header = _b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    claims = _b64(json.dumps({
        "iss": info["client_email"],
        "scope": " ".join(scopes),
        "aud": "https://oauth2.googleapis.com/token",
        "iat": now,
        "exp": now + 3600,
    }).encode())
    signing_input = f"{header}.{claims}".encode()
    key_file = tempfile.NamedTemporaryFile("w", delete=False)
    try:
        key_file.write(info["private_key"])
        key_file.close()
        signature = subprocess.check_output(
            ["openssl", "dgst", "-sha256", "-sign", key_file.name],
            input=signing_input,
        )
    finally:
        os.unlink(key_file.name)
    assertion = signing_input.decode() + "." + _b64(signature)
    token = _post_form(
        "https://oauth2.googleapis.com/token",
        {"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer", "assertion": assertion},
        {"Content-Type": "application/x-www-form-urlencoded"},
    )
    return token["access_token"]


def user_access_token(token_path):
    with open(token_path, encoding="utf-8") as handle:
        info = json.load(handle)
    token = _post_form(
        info.get("token_uri") or "https://oauth2.googleapis.com/token",
        {
            "client_id": info["client_id"],
            "client_secret": info["client_secret"],
            "refresh_token": info["refresh_token"],
            "grant_type": "refresh_token",
        },
        {"Content-Type": "application/x-www-form-urlencoded"},
    )
    return token["access_token"]


def get_json(url, access_token):
    request = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            return response.status, json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        raise RuntimeError(f"Google {error.code}: {body[:180]}") from None


def post_json(url, access_token, payload):
    data = json.dumps(payload).encode()
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        raise RuntimeError(f"Google {error.code}: {body[:180]}") from None


def put_json(url, access_token, payload):
    data = json.dumps(payload).encode()
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
        method="PUT",
    )
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        raise RuntimeError(f"Google {error.code}: {body[:180]}") from None
