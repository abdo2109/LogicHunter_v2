# LogicHunter v2 🦇

**AI-Orchestrated Bug Bounty Framework (Web2 + Web3)**
*From Recon → Exploitation → Validation → Report*

> Dynamic AI Brains · Model Routing · Logic-Based Attack Modules · AI-Assisted Reporting

LogicHunter is not a scanner.
It’s a **decision engine + execution pipeline** built for hunters who deal with large recon data and need to prioritize, test, and validate efficiently.

Instead of hardcoding a static methodology, LogicHunter:

* reads your recon output
* maps attack surfaces using dynamic `skills/`
* triggers targeted attack modules
* filters weak signals
* helps you generate structured reports

---

## ⚠️ What This Tool Actually Does

LogicHunter does NOT magically find bugs.

It helps you:

* reduce noise from recon
* focus on high-probability attack paths
* automate repetitive attack patterns
* structure findings into reports

You still need:

> manual validation + real attacker thinking

---

## 🧠 Why Google Gemini? (And Can I Use Claude?)

In bug bounty, context matters more than anything.

LogicHunter uses **Google Gemini** because:

1. **Large Context Handling**

   * Can process huge recon outputs (JS files, URLs, Burp logs)

2. **Model Routing**

   * Cheap models for parsing
   * Better models for reasoning & reporting

3. **Speed**

   * Fast responses when dealing with large inputs

### Can I use Claude?

Yes.

The architecture is modular:

* Replace logic inside `ai_engine.py`
* Keep everything else (skills, tools, flow)

---

## 🏗 Architecture & Workflow

```text
Target ──▶ Recon ──▶ Brain (Skill Load) ──▶ Attack ──▶ Validate ──▶ Report
           │                │                  │           │            │
           │                │                  │           │            └── zero_report.py
           │                │                  │           └── validator_agent (AI-assisted)
           │                │                  └── zero_* modules (IDOR / Race / Fuzzer)
           │                └── skills/*.md (methodology)
           └── subfinder + httpx + nuclei + katana + ffuf + zero_dork.py
```

---

## ⚙️ How It Actually Works (Deep Dive)

1. Recon data is collected (subdomains, URLs, JS, etc.)

2. `recon_agent` parses and summarizes targets:

   * endpoints
   * parameters
   * auth-required routes

3. Selected skill (`skills/*.md`) defines attack methodology

4. AI maps:

   * endpoint → possible vuln class
   * parameters → attack surface

5. Attack module is triggered:

   * IDOR → `zero_idor.py`
   * Race → `zero_race.py`
   * Logic fuzz → `attack_fuzzer.py`

6. Output is analyzed:

   * weak signals dropped
   * interesting signals flagged

7. Report is generated using `zero_report.py`

---

## 🧠 Skills (Dynamic Brains)

LogicHunter adapts based on loaded methodology.

| Skill                | Purpose              |
| -------------------- | -------------------- |
| web2-recon.md        | Recon workflows      |
| web2-vuln-classes.md | Bug class checklists |
| web3-audit.md        | Smart contract logic |
| Custom               | Your own methodology |

> `skills/` = your real power

---

## ⚔️ Tool Reference

### Core Pipeline

| Tool           | Role             |
| -------------- | ---------------- |
| logichunter.py | CLI orchestrator |
| ai_engine.py   | AI integration   |
| zero_report.py | Report generator |

---

### Attack Modules (Realistic View)

| Tool             | What It Does                                                   |
| ---------------- | -------------------------------------------------------------- |
| zero_idor.py     | Token swapping + response comparison (needs manual validation) |
| zero_race.py     | Parallel requests (basic race testing, not advanced sync)      |
| attack_fuzzer.py | Parameter + method mutation                                    |
| zero_sneaky.py   | Unicode-based payload obfuscation (niche use)                  |
| zero_dork.py     | Targeted Google dorking                                        |
| zero_cve.py      | Nuclei wrapper for critical CVEs                               |

---

## 🤖 Agents (Model Routing)

| Agent           | Role                       |
| --------------- | -------------------------- |
| recon_agent     | parses large data          |
| validator_agent | analyzes & filters signals |
| report_writer   | generates reports          |

---

## 🚀 Quick Start

```bash
git clone https://github.com/abdo2109/LogicHunter_v2.git
cd LogicHunter_v2

chmod +x install.sh
./install.sh

pip install -r requirements.txt
```

---

## 🧪 Usage

```bash
python3 logichunter.py
```

Commands:

* `hunt target.com`
* `recon`
* `brains`
* `attack`
* `report`

---

## 📁 Directory Structure

```text
LogicHunter_v2/
├── logichunter.py
├── ai_engine.py
├── config.json
├── install.sh
├── requirements.txt
│
├── zero_dork.py
├── zero_cve.py
├── zero_idor.py
├── zero_race.py
├── zero_sneaky.py
├── attack_fuzzer.py
├── zero_report.py
│
├── skills/
├── wordlists/
├── findings/
└── reports/
```

---

## ⚖️ Rules of Engagement

* Respect scope
* No out-of-scope testing
* Authorized targets only
* Follow responsible disclosure

---

## 🧠 Final Note

LogicHunter is built to assist hunters — not replace them.

Use it to:

* think faster
* test smarter
* reduce noise
