#!/usr/bin/env python3
"""
Zero Race Condition Tester - Universal Parallel Request Spammer
Created for LogicHunter Framework
"""
import argparse
import requests
import concurrent.futures
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def print_banner():
    print("\033[91m[*] Zero Universal Race Condition Spammer\033[0m")

def send_req(url, method, headers, data):
    try:
        if method.upper() == "GET":
            r = requests.get(url, headers=headers, verify=False, timeout=5)
        else:
            r = requests.request(method.upper(), url, headers=headers, data=data, verify=False, timeout=5)
        return r.status_code, len(r.text)
    except:
        return 000, 0

def test_race(url, method, data, token, threads):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    print(f"[\033[93m+\033[0m] Target: {url}")
    print(f"[\033[94m*\033[0m] Firing {threads} parallel requests... Hold tight!\n")
    
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(send_req, url, method, headers, data) for _ in range(threads)]
        for future in concurrent.futures.as_completed(futures):
            status, length = future.result()
            key = f"Status: {status} | Length: {length}"
            results[key] = results.get(key, 0) + 1

    print("\033[92m[=== RACE CONDITION RESULTS ===]\033[0m")
    for res, count in results.items():
        print(f"  -> {count} requests returned: [{res}]")
        
    print("\n\033[93m[Tip]\033[0m If you see 1 success (200) and the rest are errors (400/429), it's secure.")
    print("\033[93m[Tip]\033[0m If you see MULTIPLE successes (200) for a single-use action (like using a coupon), YOU FOUND A RACE CONDITION!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-m", "--method", default="POST", help="HTTP Method (POST, PUT)")
    parser.add_argument("-d", "--data", default="", help="JSON Data payload")
    parser.add_argument("-t", "--token", required=True, help="Your Authorization Bearer Token")
    parser.add_argument("-c", "--count", type=int, default=20, help="Number of parallel requests")
    args = parser.parse_args()
    
    print_banner()
    test_race(args.url, args.method, args.data, args.token, args.count)
