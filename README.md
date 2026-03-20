

# LogicHunter_V2 🦇

**AI-Orchestrated Bug Bounty Framework (Web2 + Web3)**
*From Recon → Exploitation → Validation → Report*

> Not another scanner. This is a **decision engine + execution pipeline**.

---

## ⚠️ What This Actually Is (No BS)

LogicHunter does NOT magically find bugs.

It:

* reads recon output
* prioritizes attack surface
* executes targeted modules
* validates signals
* produces structured reports

Everything is built around one idea:

> **Stop wasting time on weak signals.**

---

## 🧠 Core Philosophy

Most tools:

> run → dump results → you manually think

LogicHunter:

> think → choose attack → execute → validate → report

---

## 🏗 Real Workflow

```text
Recon Data → AI Decision → Targeted Attack → Signal → Validation → Report
```

NOT:

> spam everything and pray

---

## 🔥 Where It Actually Helps

* Large recon outputs (10k+ URLs / JS / subdomains)
* Prioritizing attack vectors (IDOR vs SSRF vs Logic)
* Killing false positives early
* Structuring reports fast

---

## ❌ Where It DOES NOT Help

* It won't replace manual logic thinking
* It won't magically find 0days
* It won't bypass auth unless the target is actually vulnerable

لو حد مش فاهم النقطة دي، الأداة دي مش ليه.

---

## ⚔️ Attack Modules (Reality Check)

### `zero_idor.py`

* Uses: token swapping + response diffing
* Weakness: naive length-only detection is NOT enough
* You should validate manually or extend with JSON diffing

---

### `zero_race.py`

* Uses: parallel requests
* Reality: NOT true race condition exploitation (no sync primitives)
* Useful for: low-hanging race bugs only

---

### `attack_fuzzer.py`

* Mutates parameters + methods
* Good for:

  * edge cases
  * logic breaks
* NOT a replacement for Burp Intruder/Turbo Intruder

---

### `zero_sneaky.py`

* Unicode payload obfuscation
* Niche use-case (WAF / LLM bypass)
* Don't expect magic results everywhere

---

## 🤖 AI Layer (Important)

AI is used for:

* prioritization
* reasoning
* filtering
* report drafting

AI is NOT:

* a source of truth
* always correct
* safe from hallucination

---

## 🚀 Quick Start (FIXED)

```bash
git clone https://github.com/abdo2109/LogicHunter_v2.git
cd LogicHunter_v2

chmod +x install.sh
./install.sh

pip install -r requirements.txt
```

---

## 🧪 Example Use (Realistic)

```bash
python3 logichunter.py
```

```bash
hunt target.com
recon
attack
```

Expected:

* NOT instant bugs
* BUT structured attack direction

---

## 🧠 Skills (Your Real Power)

The strongest part of LogicHunter:

> `skills/` = your brain

Add:

* your recon methodology
* your bug hunting patterns
* your checklists

This is what actually scales your hunting.

---

## 📌 What You Should Do As A Hunter

Don't just run it.

Use it to:

* guide thinking
* speed execution
* reduce noise

---

## ⚖️ Legal

