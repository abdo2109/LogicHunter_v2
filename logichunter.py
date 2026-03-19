#!/usr/bin/env python3
import os
import sys
import subprocess
from ai_engine import LogicHunterAI

# إجبار بايثون على استخدام UTF-8 لدعم اللغة العربية في الإدخال والإخراج
try:
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
R = '\033[91m'
W = '\033[0m'

def banner():
    print(f"""{B}
 _                 _      _   _             _            
| |               (_)    | | | |           | |           
| |     ___   __ _ _  ___| |_| |_   _ _ __ | |_ ___ _ __ 
| |    / _ \\ / _` | |/ __|  _  | | | | '_ \\| __/ _ \\ '__|
| |___| (_) | (_| | | (__| | | | |_| | | | | ||  __/ |   
\\_____/\\___/ \\__, |_|\\___\\_| |_/\\__,_|_| |_|\\__\\___|_|   
              __/ |                                      
             |___/                                       
    {W}
    {Y}Advanced AI-Powered Bug Bounty Framework - Powered by Gemini{W}
    
    "Logic is my only weapon." - Ayanokoji Kiyotaka
    {B}Developed by: 0xHamid (Zero){W}
    """)

def show_main_help():
    print(f"""
{Y}=== Global Commands ==={W}
  {G}hunt <target>{W}  : Start a deep hunting session on a specific target
  {G}clear{W}          : Clear the terminal screen
  {G}help{W}           : Show this global menu
  {G}exit / quit{W}    : Turn off LogicHunter
    """)

def show_session_help():
    print(f"""
{Y}=== Session Commands (Context: Active) ==={W}
  {G}recon{W}          : Run Subfinder + Feed data to AI for analysis
  {G}tools{W}          : Open the manual tools execution menu (Nuclei, Ffuf, Dorks, etc.)
  {G}attack{W}         : Open the Advanced Custom Attack Modules (IDOR, Race, etc.)
  {G}brains{W}         : List all available AI Skills & Methodologies (Web2, Web3, etc.)
  {G}brain <id>{W}     : Switch the AI's Brain/Context to a specific skill
  {G}chat <msg>{W}     : Chat directly with the AI about this target
  {G}report{W}         : Generate a professional HackerOne Markdown report via AI
  {G}clear{W}          : Clear the terminal screen
  {G}back{W}           : Save session context & return to main menu
  {G}help{W}           : Show this session menu
    """)

def get_available_skills():
    """Scans the skills directory for all .md files dynamically."""
    skills = []
    if os.path.exists("skills"):
        for root, dirs, files in os.walk("skills"):
            for file in files:
                if file.endswith(".md"):
                    skills.append(os.path.join(root, file))
    return sorted(skills)

def run_tools_menu(target):
    while True:
        print(f"\n{Y}=== Interactive Tools Menu ({target}) ==={W}")
        print(f"  1. {B}subfinder{W}  (Subdomain Enumeration)")
        print(f"  2. {B}httpx{W}      (Live Host Discovery)")
        print(f"  3. {B}nuclei{W}     (Template Vulnerability Scanner)")
        print(f"  4. {B}katana{W}     (Web Crawler / Endpoints)")
        print(f"  5. {B}ffuf{W}       (Directory/Endpoint Fuzzing - Custom Wordlist)")
        print(f"  6. {B}arjun{W}      (Parameter Discovery)")
        print(f"  7. {B}Zero Dorks{W} (Google Dorks Links Generator)")
        print(f"  8. {B}Zero CVE{W}   (High/Critical CVE Scanner)")
        print(f"  0. {R}Back to Session{W}")
        
        choice = input(f"\n{G}Select Tool (0-8){W} > ").strip()
        
        if choice == '1':
            os.system(f"subfinder -d {target}")
        elif choice == '2':
            os.system(f"echo {target} | httpx")
        elif choice == '3':
            os.system(f"nuclei -u {target}")
        elif choice == '4':
            os.system(f"katana -u https://{target}")
        elif choice == '5':
            if os.path.exists("wordlists"):
                wordlists = sorted([f for f in os.listdir("wordlists") if f.endswith(".txt")])
                if not wordlists:
                    print(f"[{R}-{W}] No .txt files found in wordlists/ directory.")
                else:
                    print(f"\n{Y}=== Available Wordlists ==={W}")
                    for idx, wl in enumerate(wordlists):
                        print(f"  [{idx}] {B}{wl}{W}")
                    
                    wl_choice = input(f"\n{G}Select Wordlist number{W} > ").strip()
                    if wl_choice.isdigit() and 0 <= int(wl_choice) < len(wordlists):
                        selected_wl = os.path.join("wordlists", wordlists[int(wl_choice)])
                        print(f"[{B}*{W}] Starting ffuf using {selected_wl}...")
                        os.system(f"ffuf -u https://{target}/FUZZ -w {selected_wl} -mc 200,301,302,403,500")
                    else:
                        print(f"[{R}-{W}] Invalid wordlist choice.")
            else:
                print(f"[{R}-{W}] Folder 'wordlists' not found!")
                
        elif choice == '6':
            os.system(f"arjun -u https://{target}")
        elif choice == '7':
            os.system(f"python3 zero_dork.py {target}")
        elif choice == '8':
            os.system(f"python3 zero_cve.py https://{target}")
        elif choice == '0':
            break
        else:
            print(f"[{R}-{W}] Invalid choice.")

def run_attack_modules(target):
    while True:
        print(f"\n{R}=== Advanced Attack Modules ({target}) ==={W}")
        print(f"  1. {B}Zero Sneaky Bits{W}   (Invisible Prompt Injection & WAF Bypass)")
        print(f"  2. {B}Zero IDOR Scanner{W}  (Cross-User Authorization Tester)")
        print(f"  3. {B}Zero Race Condition{W}(Parallel Request Spammer)")
        print(f"  4. {B}Zero-Day Fuzzer{W}    (Logic Bugs & Edge Cases)")
        print(f"  0. {G}Back to Session{W}")
        
        choice = input(f"\n{R}Select Module (0-4){W} > ").strip()
        
        if choice == '1':
            print(f"\n[{B}*{W}] Zero Sneaky Bits (Invisible Payload Generator)")
            action = input(f"[{Y}?{W}] Enter action (encode / decode / generate / test) : ").strip().lower()
            
            if action == 'encode':
                text = input(f"[{Y}?{W}] Enter text to hide: ").strip()
                os.system(f"python3 zero_sneaky.py encode \"{text}\"")
            elif action == 'decode':
                text = input(f"[{Y}?{W}] Enter text to decode: ").strip()
                os.system(f"python3 zero_sneaky.py decode \"{text}\"")
            elif action == 'generate':
                payload = input(f"[{Y}?{W}] Payload to disguise (e.g. <script>alert(1)</script>) : ").strip()
                os.system(f"python3 zero_sneaky.py generate \"{payload}\"")
            elif action == 'test':
                os.system("python3 zero_sneaky.py test")
            else:
                print(f"[{R}-{W}] Invalid action. Returning to menu.")
            
        elif choice == '2':
            print(f"\n[{B}*{W}] Zero IDOR Scanner.")
            url = input(f"[{Y}?{W}] Enter Target Endpoint (e.g. https://api.{target}/user/123) : ").strip()
            token_a = input(f"[{Y}?{W}] Enter Token A (Victim)   : ").strip()
            token_b = input(f"[{Y}?{W}] Enter Token B (Attacker) : ").strip()
            
            if url and token_a and token_b:
                print(f"\n{Y}[!] تحذير هـام جداً قبل التنفيذ:{W}")
                print(f"{Y}السكريبت بيعتمد على تطابق حجم الرد (Response Length). أحياناً السيرفر بيعمل Redirect لصفحة الـ Home أو الـ Login{W}")
                print(f"{Y}وبيكون حجمهم متطابق، فتبان إنها ثغرة IDOR وهي (False Positive). لازم تراجع الريكويست بنفسك في Burp Suite.{W}")
                print(f"{Y}(إحنا مبعتناش الرد لـ Gemini عشان نحافظ على التوكنز من الحرق على الفاضي).{W}\n")
                
                input(f"[{B}*{W}] Press ENTER to start the IDOR attack...")
                os.system(f"python3 zero_idor.py -u {url} -ta {token_a} -tb {token_b}")
            else:
                print(f"[{R}-{W}] Missing inputs. Aborting.")
                
        elif choice == '3':
            print(f"\n[{B}*{W}] Zero Race Condition Tester.")
            url = input(f"[{Y}?{W}] Enter Target Endpoint (e.g. https://api.{target}/redeem) : ").strip()
            token = input(f"[{Y}?{W}] Enter Auth Token : ").strip()
            
            if url and token:
                os.system(f"python3 zero_race.py -u {url} -t {token}")
            else:
                print(f"[{R}-{W}] Missing inputs. Aborting.")
                
        elif choice == '4':
            print(f"\n[{B}*{W}] Firing Zero-Day Fuzzer at {target}...")
            os.system(f"python3 zero_fuzzer.py https://{target}")
            
        elif choice == '0':
            break
        else:
            print(f"[{R}-{W}] Invalid choice.")

def target_session(target, ai):
    print(f"\n[{B}*{W}] Entering War Room for: {Y}{target}{W}")
    
    all_skills = get_available_skills()
    
    default_skill = "skills/web2-recon/SKILL.md"
    if default_skill not in all_skills and all_skills:
        default_skill = all_skills[0]
        
    ai_session = None
    if all_skills:
        print(f"[{G}+{W}] Loading default AI Brain: {default_skill}")
        # تم التعديل هنا: استخدام موديل validator_agent الأساسي
        ai_session = ai.start_hunt_session("validator_agent", default_skill)
    else:
        print(f"[{R}!{W}] No skills found in 'skills/' directory. Running with basic AI context.")
        ai_session = ai.model.start_chat(history=[])
    
    while True:
        try:
            cmd_input = input(f"\n{G}LogicHunter ({target}){W} > ").strip()
            if not cmd_input:
                continue
                
            parts = cmd_input.split()
            command = parts[0].lower()

            if command == "back":
                print(f"[{B}*{W}] Pausing session. Returning to Global Menu...")
                break
                
            elif command == "help":
                show_session_help()
                
            elif command == "clear":
                os.system('clear')
                
            elif command == "tools":
                run_tools_menu(target)
                
            elif command == "attack":
                run_attack_modules(target)
                
            elif command == "brains":
                print(f"\n{Y}=== Available AI Brains (Skills Library) ==={W}")
                if not all_skills:
                    print(f"  {R}No .md files found in skills/ directory.{W}")
                else:
                    for idx, skill in enumerate(all_skills):
                        print(f"  [{idx}] {B}{skill}{W}")
                print(f"{Y}============================================{W}")
                print(f"Use '{G}brain <number>{W}' to switch the AI's context.")

            elif command == "brain":
                if len(parts) < 2 or not parts[1].isdigit():
                    print(f"[{R}-{W}] Usage: brain <number> (type 'brains' to see the list)")
                    continue
                
                idx = int(parts[1])
                if 0 <= idx < len(all_skills):
                    selected_skill = all_skills[idx]
                    print(f"[{B}*{W}] Switching AI Brain to: {Y}{selected_skill}{W} ...")
                    # تم التعديل هنا: استخدام موديل validator_agent عند التبديل
                    ai_session = ai.start_hunt_session("validator_agent", selected_skill)
                    print(f"[{G}+{W}] Brain loaded successfully! The AI is now an expert in this specific field.")
                else:
                    print(f"[{R}-{W}] Invalid brain number.")
                
            elif command == "recon":
                print(f"[{G}+{W}] Running Subfinder on {target}...")
                result = subprocess.run(['subfinder', '-d', target, '-silent'], capture_output=True, text=True)
                subdomains = result.stdout.strip()
                
                if not subdomains:
                    print(f"[{R}-{W}] No subdomains found.")
                    continue
                    
                print(f"[{G}+{W}] Found subdomains. Sending top 20 to AI (saving tokens)...")
                limited_subs = "\n".join(subdomains.split('\n')[:20]) 
                
                prompt = f"Target: {target}\nHere are some discovered subdomains:\n{limited_subs}\nAnalyze them based on your methodology."
                
                # تم التعديل هنا: توجيه الريكويست المليان داتا لموديل recon_agent (Flash Lite)
                recon_response = ai.ask_agent("recon_agent", prompt)
                
                print(f"\n{Y}=== [ AI INTELLIGENCE REPORT ] ==={W}\n{recon_response}\n{Y}=================================={W}")
            
            elif command == "chat":
                msg = " ".join(parts[1:])
                if not msg:
                    print(f"[{R}-{W}] Usage: chat <your question to the AI>")
                    continue
                print(f"[{B}*{W}] Thinking...")
                response = ai_session.send_message(msg)
                print(f"\n{Y}AI:{W}\n{response.text}")
                
            elif command == "report":
                vuln = input(f"[{Y}?{W}] Enter Vulnerability Name (e.g. XSS in Search) : ").strip()
                desc = input(f"[{Y}?{W}] Enter brief description or PoC              : ").strip()
                if vuln and desc:
                    os.system(f"python3 zero_report.py -v \"{vuln}\" -d \"{desc}\"")
                else:
                    print(f"[{R}-{W}] Missing inputs. Cancelled.")
                
            else:
                print(f"[{R}-{W}] Unknown session command. Type 'help'.")

        except UnicodeDecodeError:
            print(f"[{R}!{W}] Terminal Encoding Error! Please avoid typing Arabic characters if your terminal doesn't support UTF-8 natively.")
            continue
        except KeyboardInterrupt:
            print(f"\n[{B}*{W}] Press 'back' to return, or exit.")

def main():
    os.system('clear')
    banner()
    
    print(f"[{B}*{W}] Booting LogicHunter AI Core...")
    ai = LogicHunterAI()
    print(f"[{G}+{W}] Systems Online. Type 'help' for commands.\n")
    
    while True:
        try:
            cmd_input = input(f"{B}LogicHunter{W} > ").strip()
            if not cmd_input:
                continue
                
            parts = cmd_input.split()
            command = parts[0].lower()
            
            if command in ["exit", "quit"]:
                print(f"\n[{B}*{W}] Shutting down. Happy Hunting!")
                break
                
            elif command == "help":
                show_main_help()
                
            elif command == "clear":
                os.system('clear')
                
            elif command == "hunt":
                if len(parts) < 2:
                    print(f"[{R}-{W}] Usage: hunt <target.com>")
                else:
                    target_session(parts[1], ai)
                    
            else:
                print(f"[{R}-{W}] Unknown command. Type 'help'.")
                
        except UnicodeDecodeError:
            print(f"[{R}!{W}] Terminal Encoding Error! Please avoid typing Arabic characters if your terminal doesn't support UTF-8 natively.")
            continue
        except KeyboardInterrupt:
            print(f"\n[{B}*{W}] Shutting down. Happy Hunting!")
            break

if __name__ == "__main__":
    main()