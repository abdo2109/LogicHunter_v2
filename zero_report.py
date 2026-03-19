#!/usr/bin/env python3
"""
Zero AI Report Generator
Created for LogicHunter Framework
"""
import argparse
import os
from ai_engine import LogicHunterAI

def generate_report(vuln_name, description):
    print("\n\033[94m[*] Zero AI Report Generator\033[0m")
    print("\033[93m[*] Waking up the Report Writer Agent...\033[0m")
    
    ai = LogicHunterAI()
    prompt = f"""
    You are an elite Bug Bounty hunter. Write a highly professional HackerOne bug report for the following vulnerability.
    
    Vulnerability Name: {vuln_name}
    Details / PoC: {description}
    
    Please format the report in Markdown using this exact structure:
    # Title
    ## Summary
    ## Description
    ## Steps To Reproduce
    ## Impact
    ## Mitigation
    """
    
    # بنستخدم الموديل 2.5-flash المخصص للتقارير
    response = ai.ask_agent("report_writer", prompt)
    
    os.makedirs("reports", exist_ok=True)
    filename = f"reports/Zero_{vuln_name.replace(' ', '_')}.md"
    
    with open(filename, "w") as f:
        f.write(response)
        
    print(f"\n\033[92m[+] BOOM! Professional report generated successfully!\033[0m")
    print(f"\033[92m[+] Saved to: {filename}\033[0m\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vuln", required=True, help="Vulnerability Name (e.g., 'IDOR in Profile')")
    parser.add_argument("-d", "--desc", required=True, help="Proof of concept or short description")
    args = parser.parse_args()
    generate_report(args.vuln, args.desc)
