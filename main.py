# main.py
import argparse
from MODULES import port_scanner, banner_grabber, bruteforce_demo, reporter, vuln_checks, logger_mod
from MODULES import reporter as rep
from datetime import datetime
import os

logger = logger_mod.get_logger()

def run_scan(args):
    host = args.host
    if args.common:
        ports = port_scanner.common_ports()
    else:
        ports = list(range(args.start, args.end+1))
    logger.info(f"Scanning {host} ports: {ports}")
    results = port_scanner.scan_ports(host, ports, threads=args.threads)
    # Grab banners for open ports
    banners = {}
    for p, open_ in results.items():
        if open_:
            banners[p] = banner_grabber.grab_banner(host, p)
    # Print summary
    for p in sorted(results):
        if results[p]:
            logger.info(f"Port {p}: OPEN")
        else:
            logger.debug(f"Port {p}: closed")
    # Save reports
    prefix = args.report_prefix or f"report_{host}"
    html_name = rep.timestamped_name(prefix, "html")
    sections = {
        "Port Scan Results": "\n".join(f"{p}: {'open' if results[p] else 'closed'}" for p in sorted(results)),
        "Banners": "\n".join(f"{p}: {banners.get(p,'')}" for p in sorted(banners))
    }
    rep.generate_html_report(html_name, f"Scan report for {host}", sections)
    logger.info(f"Saved HTML report: {html_name}")

    if args.save_csv:
        csv_name = rep.timestamped_name(prefix, "csv")
        rows = []
        for p in sorted(results):
            rows.append({"port": p, "open": results[p], "banner": banners.get(p, "")})
        rep.generate_csv_report(csv_name, rows, headers=["port", "open", "banner"])
        logger.info(f"Saved CSV report: {csv_name}")

def run_bruteforce(args):
    url = args.url
    username = args.username
    if args.passfile:
        with open(args.passfile, "r") as f:
            pwds = [l.strip() for l in f if l.strip()]
    else:
        pwds = ["123456", "password", "admin", "secret123"]
    logger.warning("** WARNING: This demo only targets localhost by default. **")
    if not url.startswith("http://127.0.0.1") and not url.startswith("http://localhost"):
        logger.error("By default this toolkit refuses to attack remote hosts. Edit the code only if you have explicit permission.")
        return
    successes = bruteforce_demo.dictionary_attack(url, username, pwds)
    logger.info(f"Bruteforce successes: {successes}")
    prefix = args.report_prefix or "bruteforce_report"
    html_name = rep.timestamped_name(prefix, "html")
    sections = {
        "Attempted logins": "\n".join(f"{username}:{p}" for p in pwds),
        "Successes": str(successes)
    }
    rep.generate_html_report(html_name, "Bruteforce Report", sections)
    logger.info(f"Saved report: {html_name}")

def run_vuln(args):
    host = args.host
    port = args.port
    logger.info(f"Running simple vulnerability checks against {host}:{port}")
    findings = vuln_checks.http_basic_checks(host, port)
    # Print findings
    for k, v in findings.items():
        logger.info(f"{k}: {v}")
    # Save report
    prefix = args.report_prefix or f"vuln_{host}_{port}"
    html_name = rep.timestamped_name(prefix, "html")
    sections = {"Vuln Findings": "\n".join(f"{k}: {v}" for k, v in findings.items())}
    rep.generate_html_report(html_name, f"Vuln findings for {host}:{port}", sections)
    logger.info(f"Saved vulnerability report: {html_name}")

def main():
    parser = argparse.ArgumentParser(description="Basic PenTesting Toolkit (educational) - extended")
    sub = parser.add_subparsers(dest="cmd")

    p_scan = sub.add_parser("scan", help="Port scan")
    p_scan.add_argument("--host", required=True)
    p_scan.add_argument("--common", action="store_true", help="Scan common ports")
    p_scan.add_argument("--start", type=int, default=1)
    p_scan.add_argument("--end", type=int, default=1024)
    p_scan.add_argument("--threads", type=int, default=100, help="Worker threads for scanning")
    p_scan.add_argument("--save-csv", action="store_true", help="Also save CSV output")
    p_scan.add_argument("--report-prefix", help="Prefix for report files (timestamp appended)")

    p_bf = sub.add_parser("brute", help="Safe brute-force demo (localhost only)")
    p_bf.add_argument("--url", required=True)
    p_bf.add_argument("--username", required=True)
    p_bf.add_argument("--passfile", help="Optional password file (one per line)")
    p_bf.add_argument("--report-prefix", help="Prefix for report files (timestamp appended)")

    p_vuln = sub.add_parser("vuln", help="Run simple, safe vulnerability checks")
    p_vuln.add_argument("--host", required=True)
    p_vuln.add_argument("--port", type=int, required=True)
    p_vuln.add_argument("--report-prefix", help="Prefix for report files (timestamp appended)")

    args = parser.parse_args()
    if args.cmd == "scan":
        run_scan(args)
    elif args.cmd == "brute":
        run_bruteforce(args)
    elif args.cmd == "vuln":
        run_vuln(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
