# modules/banner_grabber.py
"""
Attempt to fetch a banner from a TCP service by connecting and reading bytes.
Often servers send a banner (SMTP, FTP, some HTTP servers).
"""

import socket

def grab_banner(host: str, port: int, timeout: float = 1.0) -> str:
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((host, port))
        # Try reading some bytes (not all services will send data)
        try:
            data = s.recv(1024)
            return data.decode(errors='ignore').strip()
        except socket.timeout:
            return ""
        finally:
            s.close()
    except Exception as e:
        return ""
