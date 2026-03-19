# LogicHunter 🦇

**The Advanced AI-Powered Bug Bounty Framework. Web2 + Web3. Recon to Report.** *Built for the modern hacker.*

[](https://www.python.org/downloads/)
[](https://deepmind.google/technologies/gemini/)
[](https://opensource.org/licenses/MIT)

> **Dynamic AI Brains · Model Routing · Zero-Day Weapons · AI Report Generator**

Most bug bounty toolkits give you a bag of scattered scripts. LogicHunter gives you an **AI-Orchestrated Agent Harness** that reasons about attack surfaces, validates what you find, deploys custom zero-day weapons, and writes reports that pay.

Instead of hardcoding a methodology, LogicHunter reads your recon output, maps it to the highest-ROI attack surface via dynamically loaded "Brains" (`skills/`), and drives custom tools to kill weak findings before you waste time writing them up.

-----

## 🧠 Why Google Gemini? (And Can I Use Claude?)

In Bug Bounty, context is everything. We chose **Google Gemini** as the core AI engine for three critical reasons:

1.  **The Massive Context Window:** Gemini offers up to **2 Million tokens**. You can dump entire JavaScript bundles, massive `httpx` outputs, thousands of subdomains, or raw Burp Suite HTTP histories directly into the prompt without the model "forgetting" the beginning.
2.  **Cost-Effective Model Routing:** LogicHunter uses a smart `config.json` router. It sends massive, noisy recon data to `gemini-3.1-flash-lite-preview` (cheap & fast), complex logic analysis to `gemini-3-flash-preview`, and report drafting to `gemini-2.5-flash` (high quality).
3.  **Speed & Native Audio/Video:** Gemini's response time for large datasets outpaces competitors, which is crucial for live, parallel hunting.

**Want to use Claude (Anthropic) instead?** Absolutely. LogicHunter's architecture is deeply modular (ECC-Style Plugin Architecture). You can easily swap the AI core by modifying the `ai_engine.py` file to use the `anthropic` SDK while keeping the entire framework, tools, prompts, and `skills/` directory completely intact.

-----

## 🏗 Architecture & Workflow

```text
Target ──▶ Recon ──▶ Brain (Skill Load) ──▶ Attack/Fuzz ──▶ Validate ──▶ Report
           │                │                    │             │            │
           │                │                    │             │            └── zero_report.py
           │                │                    │             └── validator_agent (AI)
           │                │                    └── zero_sneaky.py / zero_idor.py / zero_race.py
           │                └── skills/*.md (Web2, Web3, Smart Contracts, Custom Logic)
           └── subfinder + httpx + nuclei + katana + ffuf + zero_dork.py
```

### Why this beats scattered scripts:

| Problem with scripts | How LogicHunter solves it |
| :--- | :--- |
| **No methodology** | Dynamic `skills/` directory. Load the exact methodology you need (Web2 vs Web3). |
| **False positives** | `validator_agent` analyzes outputs and kills weak findings in seconds. |
| **Reports get downgraded** | `report_writer` agent drafts H1/Bugcrowd templates with CVSS and impact language. |
| **Scattered invocations** | Everything is orchestrated from a single interactive CLI shell. |
| **Standard payloads fail** | Custom "Zero" tools (e.g., Invisible prompt injection, Race Condition spammer). |

-----

## 🧠 Skills (Dynamic Brains)

LogicHunter doesn't force a single methodology. Drop any `.md` file into the `skills/` directory, and the AI will dynamically learn it and adopt that persona.

| Skill Domain | What It Contains | When to Use |
| :--- | :--- | :--- |
| **web2-recon.md** | Subdomain enum, live hosts, URL crawl, JS analysis, tech stack mapping. | Starting recon on a fresh target. |
| **web2-vuln-classes.md** | Checklists for IDOR, XSS, SSRF, SQLi, Race Conditions, Business Logic. | Hunting specific vulnerability classes. |
| **web3-audit.md** | DeFi bug classes, Reentrancy, Oracle Manipulation, Foundry PoC stubs. | Smart contract auditing. |
| **Custom Skills** | *Add your own\!* The AI instantly adapts to your private methodology. | Anytime you want to automate your specific workflow. |

*Type `brains` in the console to list loaded skills. Type `brain <id>` to switch the AI's persona instantly.*

-----

## ⚔️ Tool Reference

### Core Intelligence Pipeline

| Tool | Role |
| :--- | :--- |
| **`logichunter.py`** | Master orchestrator — Interactive War Room CLI. |
| **`ai_engine.py`** | GenAI integration, model routing, and context management. |
| **`zero_report.py`** | Outputs formatted HackerOne/Bugcrowd/Immunefi reports. |

### Advanced Attack Modules ("Zero" Tools)

These are custom-built, logic-based hunting scripts designed to catch what automated scanners miss:
| Tool | What It Hunts |
| :--- | :--- |
| **`zero_sneaky.py`** | **Invisible Prompt Injection & WAF Bypass.** Encodes payloads (like `<script>`) into invisible Unicode characters to bypass filters while still executing in browsers/LLMs. |
| **`zero_idor.py`** | **Logic IDOR Tester.** Takes Victim/Attacker tokens, compares response lengths dynamically, and alerts on BOLA/IDOR vulnerabilities. |
| **`zero_race.py`** | **Parallel Request Spammer.** Floods endpoints to exploit Race Conditions (TOCTOU, coupon reuse, limit overruns, 2FA bypass). |
| **`attack_fuzzer.py`** | **Smart HTTP Logic Fuzzer.** Mutates parameters, flips HTTP methods, and catches edge cases and 500 Internal Server errors. |
| **`zero_dork.py`** | **Targeted Leak Hunter.** Automates advanced Google Dorking for credentials, exposed panels, and PII leaks. |
| **`zero_cve.py`** | **Critical CVE Scanner.** Wrapper for Nuclei that specifically filters and hunts for High/Critical known CVEs. |

-----

## 🤖 Agents (Model Routing)

LogicHunter utilizes 3 specialized sub-agents defined in `config.json`.

| Agent | Role | Recommended Model |
| :--- | :--- | :--- |
| **recon\_agent** | Parses massive outputs (thousands of subdomains, `katana` crawls, raw JS). | `gemini-3.1-flash-lite-preview` (Fast & Cheap) |
| **validator\_agent** | Engages in chat, reads `skills/`, filters false positives, analyzes logic bugs. | `gemini-3-flash-preview` (Smart & Balanced) |
| **report\_writer** | Generates professional H1/Bugcrowd reports, human tone, impact-first. | `gemini-2.5-flash` (High Quality) |

-----

## 🚀 Quick Start

### 1\. Clone & Install

```bash
git clone https://github.com/YourUsername/LogicHunter.git
cd LogicHunter

# Run the installer to grab Go tools (subfinder, httpx, nuclei, ffuf, katana, arjun)
chmod +x install.sh
./install.sh

# Install Python requirements
pip install -r requirements.txt
```

### 2\. Configure API Keys

Add your Gemini API Key to `config.json`.

```json
{
  "api_keys": {
    "gemini_api_key": "AIzaSyYourKeyHere..."
  }
}
```

### 3\. Enter the War Room

```bash
python3 logichunter.py
```

**Interactive Commands:**

  * `hunt <target.com>` — Set target scope.
  * `recon` — Run full asset discovery pipeline.
  * `brains` — List available methodology files from the `skills/` folder.
  * `tools` — Open the interactive community tool menu (Subfinder, Ffuf, Nuclei, etc.).
  * `attack` — Deploy custom Zero modules (IDOR, Race Condition, Sneaky Bits).
  * `report` — Generate a submission-ready Markdown report.

-----

## 📁 Directory Structure

```text
LogicHunter/
├── logichunter.py            # Main CLI Orchestrator
├── ai_engine.py              # AI Integration (Google GenAI API)
├── config.json               # Model Routing & API Keys
├── install.sh                # Setup script for Go-based tools
├── requirements.txt          # Python dependencies
│
├── zero_dork.py              # Advanced Google Dork Automation
├── zero_cve.py               # Targeted High/Critical CVE Scanner
├── zero_idor.py              # Cross-User Authorization Tester
├── zero_race.py              # Parallel Request Spammer
├── zero_sneaky.py            # Invisible WAF Bypass Payload Generator
├── attack_fuzzer.py          # HTTP Logic Fuzzer
├── zero_report.py            # AI Report Writer / Drafter
│
├── skills/                   # [Dynamic Brains] Drop .md methodology files here
├── wordlists/                # [Ammo] Drop .txt wordlists here (auto-read by ffuf)
├── findings/                 # Output from attack modules and scanners
└── reports/                  # Generated submission-ready Markdown reports
```

-----

## ⚖️ Rules of Engagement & Legal

1.  **Read Full Scope:** Verify every asset before the first request.
2.  **Never Hunt Out-Of-Scope:** One stray request = potential ban.
3.  **Impact-First:** "What is the worst thing an attacker can do if auth is broken?" This drives your target selection.
4.  **Authorized Testing Only:** Only test targets within an approved bug bounty scope. Never test systems without explicit permission. Follow responsible disclosure practices. The authors are not responsible for any misuse.
