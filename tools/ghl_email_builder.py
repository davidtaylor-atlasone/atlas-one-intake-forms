#!/usr/bin/env python3
"""GHL Email Builder API helper. Reads GHL_PIT from .env (never prints or logs it).
Call sequence (from _briefs/assets/run-AW/RUN-GHL-JOBS-report.md):
  create: POST /emails/builder            {locationId, type:"html", title, updatedBy}
  fill:   POST /emails/builder/data       {locationId, templateId, updatedBy, editorType:"html", html, dnd:{}, previewText:""}
  list:   GET  /emails/builder            (paged)
  fetch:  the list/create response's previewUrl (plain GET, no auth header needed)
  delete: DELETE /emails/builder/{locationId}/{id}
"""
import os
import re
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
    token = env.get("GHL_PIT") or os.environ.get("GHL_PIT")
    if not token:
        return None
    return token


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


def list_templates(token, location_id=LOCATION_ID):
    """Page through GET /emails/builder. Returns a list of template summary dicts."""
    templates = []
    offset = 0
    limit = 100
    while True:
        url = f"{API_BASE}/emails/builder?locationId={location_id}&limit={limit}&offset={offset}"
        status, body = _request("GET", url, token)
        if status != 200:
            return templates, (status, body)
        page = body.get("builders") or body.get("templates") or body.get("data") or []
        if isinstance(body, list):
            page = body
        templates.extend(page)
        if len(page) < limit:
            break
        offset += limit
    return templates, (200, None)


def fetch_html(preview_url):
    """Fetch a template's rendered HTML from its previewUrl (no auth header)."""
    req = urllib.request.Request(preview_url, method="GET")
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="replace")


def create(token, title, location_id=LOCATION_ID, updated_by="atlas-one-apps"):
    url = f"{API_BASE}/emails/builder"
    body = {"locationId": location_id, "type": "html", "title": title, "updatedBy": updated_by}
    return _request("POST", url, token, body)


def fill(token, template_id, html, location_id=LOCATION_ID, updated_by="atlas-one-apps"):
    url = f"{API_BASE}/emails/builder/data"
    body = {
        "locationId": location_id,
        "templateId": template_id,
        "updatedBy": updated_by,
        "editorType": "html",
        "html": html,
        "dnd": {},
        "previewText": "",
    }
    return _request("POST", url, token, body)


def delete(token, template_id, location_id=LOCATION_ID):
    url = f"{API_BASE}/emails/builder/{location_id}/{template_id}"
    return _request("DELETE", url, token)


if __name__ == "__main__":
    tok = get_token()
    if not tok:
        sys.exit("needs .env with GHL_PIT")
    templates, err = list_templates(tok)
    if err[0] != 200:
        sys.exit(f"list failed: {err[0]} {err[1]}")
    print(f"{len(templates)} templates")
