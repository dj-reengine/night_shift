"""Read and update the Night Shift env file. Values are never logged."""

import os


def load(path):
    env = {}
    if not path or not os.path.isfile(path):
        return env
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            raw = line.strip()
            if not raw or raw.startswith("#") or "=" not in raw:
                continue
            key, value = raw.split("=", 1)
            env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def save_key(path, key, value):
    lines = []
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as handle:
            lines = handle.readlines()
    found = False
    output = []
    for line in lines:
        if line.startswith(key + "="):
            end = "\n" if line.endswith("\n") else ""
            output.append(f"{key}={value}{end}")
            found = True
        else:
            output.append(line)
    if not found:
        if output and not output[-1].endswith("\n"):
            output[-1] += "\n"
        output.append(f"{key}={value}\n")
    temporary = path + ".tmp"
    with open(temporary, "w", encoding="utf-8") as handle:
        handle.writelines(output)
    os.replace(temporary, path)


def env_path():
    return os.environ.get(
        "NIGHTSHIFT_ENV",
        os.path.expanduser("~/seafile/My Library/coding_secrets/night-shift.env"),
    )


def resolve(env, key):
    raw = env.get(key) or ""
    if not raw or os.path.isabs(raw):
        return raw
    base = os.path.dirname(env.get("_env_path") or env_path())
    return os.path.join(base, raw)
