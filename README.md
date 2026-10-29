# Corporate Bullshit Linter (`cbl`)

> *"De-masking academic gatekeeping, corporate therapy-speak, and performative posturing at machine speed."*

A ruthless, zero-dependency command-line utility that scans text files, emails, syllabi, or piped terminal streams, calculates the **Bullshit Density Score (BDS)**, and prints a decoded "Reality Translation" side-by-side in your terminal.

---

## Terminal Preview

```text
========================================================================
               CORPORATE BULLSHIT LINTER (CBL) v1.0.0
         De-masking performative rhetoric at machine speed.
========================================================================

BULLSHIT DENSITY SCORE (BDS): 100.0% [█████████████████████████]
DIAGNOSTIC STATUS: TERMINAL BULLSHIT EMERGENCY
ANALYSIS: Weaponized administrative vacuum. Reality has been completely superseded by buzzwords.
RECOMMENDED ACTION: Nuke the thread. Reject contract. Run a bash script instead.

CONTAMINATION SOURCES:
  • Academic Gatekeeping: 9 instance(s)

--- DECODED SUBTEXT TRANSLATION ---

[1] DETECTED PHRASE: "pedagogical framework" (Category: Academic Gatekeeping)
    REALITY TRANSLATION: → "arbitrary assignment rubrics made up a decade ago"

[2] DETECTED PHRASE: "prerequisite chain" (Category: Academic Gatekeeping)
    REALITY TRANSLATION: → "tuition extortion funnel forcing you into basic algebra after Calc 2"

[3] DETECTED PHRASE: "digital navigators" (Category: Academic Gatekeeping)
    REALITY TRANSLATION: → "salaried administrators paid to ignore emails"

[4] DETECTED PHRASE: "logistical complications" (Category: Academic Gatekeeping)
    REALITY TRANSLATION: → "an instructor refusing to open an email attachment"

========================================================================
```

---

## Why This Exists

Modern institutions—from community college departments to Fortune 500 corporate towers—rely on obfuscated vocabulary to evade accountability, delay decisions, and exhaust individuals into submission.

`cbl` treats performative language like compiler warnings:
1. **Regex Lexicon Matching**: Scans against three distinct taxonomies of deception.
2. **Weighted Density Scoring**: Calculates the percentage of text dedicated to evasion vs. substance.
3. **Subtext Decoding**: Replaces euphemisms with raw, unvarnished human truth.

---

## Lexicon Categories

### 1. Academic Gatekeeping & Bureaucratic Inertia
Catches administrative roadblocks used by instructors and departments:
* *"Prerequisite chain"* $\rightarrow$ *"Tuition extortion funnel forcing you into basic algebra after Calc 2"*
* *"Digital navigators"* $\rightarrow$ *"Salaried administrators paid to ignore emails"*
* *"Logistical complications"* $\rightarrow$ *"An instructor refusing to open an email attachment"*
* *"Syllabus is a contract"* $\rightarrow$ *"Rules enforced on students while the instructor ignores accommodations"*

### 2. Corporate Therapy-Speak & Managerial Dodges
Translates office jargon into plain reality:
* *"Circle back"* $\rightarrow$ *"Ignore this until everyone forgets it existed"*
* *"Touch base"* $\rightarrow$ *"Waste 15 minutes asking for an update already in Jira"*
* *"Bandwidth"* $\rightarrow$ *"Willingness to endure unpaid overtime this week"*
* *"Take this offline"* $\rightarrow$ *"Shut up before you expose management's technical ignorance"*
* *"Holding space"* $\rightarrow$ *"Staring blankly into a Zoom camera while calculating your hourly rate"*

### 3. Bourgeois Radicalism & Performative Morality
De-masks performative social posturing:
* *"Raising awareness"* $\rightarrow$ *"Wearing an ironic pastel t-shirt while accomplishing zero material change"*
* *"Centering voices"* $\rightarrow$ *"Unearned moral lecturing without doing actual manual labor"*
* *"Praxis"* $\rightarrow$ *"Argue about Sartre at a coffee shop while relying on a trust fund"*

---

## Installation & Quickstart

### 1. Direct Install
Clone this repository and symlink to your local binaries:
```bash
git clone https://github.com/patrick-isles/corporate-bullshit-linter.git
cd corporate-bullshit-linter
install -m 755 bin/cbl ~/.local/bin/cbl
```

### 2. Using Pip
```bash
pip install .
```

---

## Usage Examples

### Lint an Email File:
```bash
cbl email.txt
```

### Lint Directly via UNIX Pipes:
```bash
cat syllabus.txt | cbl
```

### Run Built-in Corporate / Academic Demo:
```bash
cbl --demo
```

### CI/CD Gatekeeping Mode:
Add `cbl --strict` to git pre-commit hooks or GitHub Actions to fail PRs with more than 15% corporate fluff:
```bash
cat release_notes.md | cbl --strict
# Exits with return code 1 if text is saturated with buzzwords
```

### Programmatic JSON Output:
```bash
cbl --json message.txt
```

---

## Author
**Patrick Isles**  
*Philosophy & Systems Engineering*  
- GitHub: [github.com/patrick-isles](https://github.com/patrick-isles)  
- LinkedIn: [linkedin.com/in/patrick-isles-78aba6232](https://www.linkedin.com/in/patrick-isles-78aba6232/)

---

## License
MIT License. Open-source, unapologetic, zero-bullshit.
