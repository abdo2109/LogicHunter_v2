#!/usr/bin/env python3
"""
Zero Dork Runner - Advanced OSINT & Dorking
Created for LogicHunter Framework
"""
import argparse
import urllib.parse

def print_banner():
    print("\033[94m[*] Zero Advanced Dork Runner\033[0m\n")

DORKS = {
    "🔑 Passwords & Secrets": [
        'site:{} ext:env | ext:yml | ext:json "password" | "api_key" | "secret"',
        'site:{} inurl:gitlab OR inurl:github "password"',
    ],
    "📂 Sensitive Directories": [
        'site:{} intitle:"index of" "parent directory"',
        'site:{} inurl:admin | inurl:dashboard | inurl:login',
    ],
    "📄 Juicy Documents": [
        'site:{} ext:pdf OR ext:xls OR ext:csv OR ext:sql "confidential" | "internal"',
    ],
    "🐛 Errors & Logs": [
        'site:{} ext:log OR ext:txt "stack trace" | "SQL syntax"',
    ]
}

def run_dorks(domain):
    print_banner()
    for category, queries in DORKS.items():
        print(f"\033[93m=== {category} ===\033[0m")
        for q in queries:
            query = q.format(domain)
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            print(f"  \033[92m[Dork]\033[0m {query}")
            print(f"  \033[90m[Link]\033[0m {url}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", help="Target domain (e.g., target.com)")
    args = parser.parse_args()
    run_dorks(args.domain)
