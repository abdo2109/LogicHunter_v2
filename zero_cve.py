#!/usr/bin/env python3
"""
Zero CVE Hunter - High/Critical Vulnerability Scanner
Created for LogicHunter Framework
"""
import argparse
import os

def run_cve_hunt(target):
    print(f"\033[94m[*] Zero CVE Hunter aiming at: {target}\033[0m")
    print(f"\033[93m[*] Firing Nuclei specifically for Critical/High CVEs...\033[0m\n")
    # بنشغل نيوكلاي ونجبره يدور في قسم الـ cves بس، وبنجيب الخطير بس عشان منضيعش وقت
    os.system(f"nuclei -u {target} -tags cve -severity critical,high")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Target URL (e.g., https://target.com)")
    args = parser.parse_args()
    run_cve_hunt(args.target)
