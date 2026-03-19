#!/usr/bin/env python3
"""
Zero IDOR Scanner - Universal Cross-User Authorization Tester
Created for LogicHunter Framework
"""
import argparse
import requests
import json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def print_banner():
    print("\033[94m[*] Zero Universal IDOR Scanner\033[0m")

def test_idor(url, method, data, token_a, token_b):
    headers_a = {"Authorization": f"Bearer {token_a}", "Content-Type": "application/json"}
    headers_b = {"Authorization": f"Bearer {token_b}", "Content-Type": "application/json"}
    
    print(f"[\033[93m+\033[0m] Target: {url}")
    print("[\033[94m*\033[0m] Sending Request as Victim (Token A)...")
    
    try:
        if method.upper() == "GET":
            res_a = requests.get(url, headers=headers_a, verify=False, timeout=10)
            res_b = requests.get(url, headers=headers_b, verify=False, timeout=10)
        else:
            res_a = requests.request(method.upper(), url, headers=headers_a, data=data, verify=False, timeout=10)
            res_b = requests.request(method.upper(), url, headers=headers_b, data=data, verify=False, timeout=10)
            
        print(f"    Victim (A)   -> Status: {res_a.status_code} | Length: {len(res_a.text)}")
        print(f"    Attacker (B) -> Status: {res_b.status_code} | Length: {len(res_b.text)}")
        
        if res_a.status_code in [200, 201] and res_b.status_code == res_a.status_code:
            if abs(len(res_a.text) - len(res_b.text)) < 50: # نسبة تفاوت بسيطة
                print("\n\033[91m[!!!] VULNERABILITY DETECTED: Potential IDOR! Attacker accessed Victim's data.\033[0m")
            else:
                print("\n\033[92m[-] No IDOR (Response lengths differ significantly).\033[0m")
        else:
            print("\n\033[92m[-] No IDOR (Access Denied or Different Status).\033[0m")
            
    except Exception as e:
        print(f"\033[91m[Error] Connection failed: {e}\033[0m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., https://api.target.com/user/123)")
    parser.add_argument("-m", "--method", default="GET", help="HTTP Method (GET, POST, PUT, DELETE)")
    parser.add_argument("-d", "--data", default="", help="JSON Data for POST/PUT requests")
    parser.add_argument("-ta", "--token-a", required=True, help="Victim's Bearer Token")
    parser.add_argument("-tb", "--token-b", required=True, help="Attacker's Bearer Token")
    args = parser.parse_args()
    
    print_banner()
    test_idor(args.url, args.method, args.data, args.token_a, args.token_b)
