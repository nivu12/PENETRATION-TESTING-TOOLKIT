# modules/port_scanner.py
"""
Simple TCP connect port scanner.
Performs a scan of ports on a host by attempting to open a TCP connection.
This is a basic technique called "connect scan" (TCP).
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    """Return True if port is open on host, False otherwise."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

def scan_ports(host: str, ports: list, threads: int = 100) -> dict:
    """
    Scan a list of ports on host.
    Returns dict: {port: True/False}
    """
    results = {}
    with ThreadPoolExecutor(max_workers=threads) as exe:
        future_to_port = {exe.submit(scan_port, host, p): p for p in ports}
        for future in as_completed(future_to_port):
            p = future_to_port[future]
            results[p] = future.result()
    return results

def common_ports():
    """Return a short list of common ports to scan (beginner-friendly)."""
    return [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
