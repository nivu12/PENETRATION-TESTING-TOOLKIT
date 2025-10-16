# modules/reporter.py
"""
Simple HTML + CSV reporter with timestamping.
"""

import csv
from datetime import datetime
from pathlib import Path

def generate_html_report(filename: str, title: str, sections: dict):
    """
    sections: dict where keys are section titles and values are strings (or HTML)
    """
    html = ["<html><head><meta charset='utf-8'><title>{}</title></head><body>".format(title)]
    html.append(f"<h1>{title}</h1>")
    html.append(f"<p>Generated: {datetime.now().isoformat(sep=' ', timespec='seconds')}</p>")
    for sec_title, content in sections.items():
        html.append(f"<h2>{sec_title}</h2>")
        html.append(f"<pre>{content}</pre>")
    html.append("</body></html>")
    Path(filename).write_text("\n".join(html), encoding="utf-8")
    return filename

def generate_csv_report(filename: str, rows: list, headers: list = None):
    """
    rows: iterable of row-lists/tuples or dicts (if headers provided)
    headers: list of column names. If given and rows are dicts, keys should match.
    """
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if headers:
            writer.writerow(headers)
            for r in rows:
                if isinstance(r, dict):
                    writer.writerow([r.get(h, "") for h in headers])
                else:
                    writer.writerow(r)
        else:
            # write rows directly
            for r in rows:
                writer.writerow(r)
    return filename

def timestamped_name(prefix: str, suffix: str):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{ts}.{suffix}"
