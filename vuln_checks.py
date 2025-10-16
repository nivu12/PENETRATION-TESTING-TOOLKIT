# modules/vuln_checks.py
"""
Very simple, safe vulnerability checks:
 - If HTTP (80/8080/443) is open, fetch / and /robots.txt
 - Record server header, presence of "Index of" (directory listing), status codes
 - If target is the local practice server (127.0.0.1:5000), optionally check known default creds (safe)
Only passive checks and basic HTTP requests.
"""

import requests
from typing import Dict

def http_basic_checks(host: str, port: int, timeout: float = 2.0) -> Dict:
    """
    host: string IP or hostname
    port: port number (integer)
    Returns a dict of findings.
    """
    findings = {"host": host, "port": port, "checked": []}
    scheme = "http"
    if port == 443:
        scheme = "https"
    base = f"{scheme}://{host}:{port}"

    try:
        r_root = requests.get(base + "/", timeout=timeout)
        findings["root_status"] = r_root.status_code
        findings["server_header"] = r_root.headers.get("Server", "")
        text = r_root.text.lower()
        findings["index_listing"] = "index of" in text  # naive directory listing detection
        findings["root_snippet"] = r_root.text[:300].replace("\n", " ")
    except Exception as e:
        findings["root_error"] = str(e)
        return findings

    # robots.txt
    try:
        r_robots = requests.get(base + "/robots.txt", timeout=timeout)
        findings["robots_status"] = r_robots.status_code
        findings["robots_body"] = r_robots.text[:500].replace("\n", " ")
    except Exception as e:
        findings["robots_error"] = str(e)

    # Extra safe check for our practice server only (127.0.0.1:5000)
    if host in ("127.0.0.1", "localhost") and port == 5000:
        findings["practice_server_detected"] = True
        # We will not brute force. Instead, verify that posting known-good creds returns 200
        try:
            r_test = requests.post(base + "/login", json={"username": "admin", "password": "secret123"}, timeout=timeout)
            findings["practice_login_status"] = r_test.status_code
            findings["practice_login_ok"] = (r_test.status_code == 200)
        except Exception as e:
            findings["practice_login_error"] = str(e)
    return findings
