#!/usr/bin/env python3
"""GHL Custom Fields API helper. Reads GHL_PIT from .env (never prints or logs it).
  list:   GET  /locations/{locationId}/customFields
  create: POST /locations/{locationId}/customFields
"""
import os
import sys
import json
import urllib.request
import urllib.error

API_BASE = "https://services.leadconnectorhq.com"
LOCATION_ID = "AzTPxnK2vSUj19jYoDmR"
API_VERSION = "2021-07-28"


def _load_env(path=None):
    path = path or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if not os.path.exists(path):
        return {}
    env = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def get_token():
    env = _load_env()
    return env.get("GHL_PIT") or os.environ.get("GHL_PIT")


def _headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Version": API_VERSION,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }


def _request(method, url, token, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(token), method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            parsed = json.loads(raw)
        except Exception:
            parsed = {"raw": raw}
        return e.code, parsed


def list_fields(token, location_id=LOCATION_ID, model="contact"):
    url = f"{API_BASE}/locations/{location_id}/customFields?model={model}"
    status, body = _request("GET", url, token)
    fields = body.get("customFields") if isinstance(body, dict) else None
    return fields or [], (status, body)


def create_field(token, name, data_type, location_id=LOCATION_ID, model="contact", parent_id=None, placeholder=None, options=None):
    url = f"{API_BASE}/locations/{location_id}/customFields"
    body = {"name": name, "dataType": data_type, "model": model}
    if parent_id:
        body["parentId"] = parent_id
    if placeholder:
        body["placeholder"] = placeholder
    if options:
        body["options"] = options
    return _request("POST", url, token, body)


def update_contact_field(token, contact_id, field_id, value):
    """PUT /contacts/{contactId}, set one custom field's value."""
    url = f"{API_BASE}/contacts/{contact_id}"
    body = {"customFields": [{"id": field_id, "field_value": value}]}
    return _request("PUT", url, token, body)


if __name__ == "__main__":
    token = get_token()
    if not token:
        print("no token", file=sys.stderr)
        sys.exit(1)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "list":
        fields, (status, raw) = list_fields(token)
        if status != 200:
            print(f"ERROR {status}: {json.dumps(raw)[:500]}", file=sys.stderr)
            sys.exit(1)
        print(json.dumps(fields, indent=2))
