# modules/logger_mod.py
"""
Simple logger wrapper. Creates console logger and a rotating file log.
Beginner-friendly: no external deps, uses Python logging only.
"""
import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name="pentoolkit"):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # avoid duplicate handlers on repeated imports

    logger.setLevel(logging.DEBUG)
    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    ch.setFormatter(ch_formatter)
    logger.addHandler(ch)

    # file handler (timestamped file)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fh = logging.FileHandler(os.path.join(LOG_DIR, f"pentoolkit_{ts}.log"), encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)

    return logger
