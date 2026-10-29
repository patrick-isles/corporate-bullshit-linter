"""
Corporate Bullshit Linter (CBL) - Analysis & Formatting Engine.
Calculates the Bullshit Density Score (BDS) and provides decoded subtext translations.
"""

import re
from typing import Dict, List, Tuple
from .dictionary import LEXICON, BSDefinition

# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"

class MatchResult:
    def __init__(self, raw: str, definition: BSDefinition, start: int, end: int):
        self.raw = raw
        self.definition = definition
        self.start = start
        self.end = end

class LintReport:
    def __init__(self, original_text: str, matches: List[MatchResult]):
        self.original_text = original_text
        self.matches = matches
        self.word_count = max(1, len(re.findall(r"\w+", original_text)))
        
        # Calculate Weighted Bullshit Density Score (BDS)
        raw_weighted_points = sum(m.definition.severity * 15 for m in matches)
        self.bds = min(100.0, round((raw_weighted_points / self.word_count) * 100, 1))
        
        # Category Breakdown
        self.categories: Dict[str, int] = {}
        for m in matches:
            cat = m.definition.category
            self.categories[cat] = self.categories.get(cat, 0) + 1

    @property
    def diagnosis(self) -> Tuple[str, str, str]:
        """Returns (Status, Diagnosis, Action)."""
        if self.bds == 0.0:
            return (
                "CLEAN (0% BDS)",
                "Raw Human Communication. Zero corporate or academic contamination detected.",
                "Execute immediately. No translation required."
            )
        elif self.bds < 15.0:
            return (
                "LOW CONTAMINATION",
                "Mild corporate buzzword leakage. Manageable with basic skepticism.",
                "Proceed with caution. Clarify vague terms before signing anything."
            )
        elif self.bds < 35.0:
            return (
                "ELEVATED TOXICITY",
                "Significant bureaucratic evasion and performative jargon present.",
                "Do not agree verbally. Demand written clarity and inspect prerequisites."
            )
        elif self.bds < 60.0:
            return (
                "CRITICAL GASLIGHTING",
                "Severe institutional rot. Text is designed to confuse, stall, and extract compliance.",
                "Escalate directly to Legal, Compliance, or ADA Disability Services."
            )
        else:
            return (
                "TERMINAL BULLSHIT EMERGENCY",
                "Weaponized administrative vacuum. Reality has been completely superseded by buzzwords.",
                "Nuke the thread. Reject contract. Run a bash script instead."
            )

def analyze_text(text: str) -> LintReport:
    matches: List[MatchResult] = []
    
    for pattern, definition in LEXICON.items():
        for match in re.finditer(pattern, text, re.IGNORECASE):
            matches.append(MatchResult(match.group(0), definition, match.start(), match.end()))
            
    # Sort matches by start position
    matches.sort(key=lambda m: m.start)
    return LintReport(text, matches)

def render_terminal(report: LintReport, plain: bool = False) -> str:
    lines: List[str] = []
    
    if plain:
        c_bold = c_reset = c_red = c_yellow = c_cyan = c_magenta = c_green = c_dim = ""
    else:
        c_bold, c_reset = BOLD, RESET
        c_red, c_yellow, c_cyan = RED, YELLOW, CYAN
        c_magenta, c_green, c_dim = MAGENTA, GREEN, DIM

    # Header Banner
    lines.append(f"{c_bold}========================================================================{c_reset}")
    lines.append(f"{c_bold}               CORPORATE BULLSHIT LINTER (CBL) v1.0.0{c_reset}")
    lines.append(f"{c_dim}         De-masking performative rhetoric at machine speed.{c_reset}")
    lines.append(f"{c_bold}========================================================================{c_reset}\n")

    # Score & Meter
    status, diag, action = report.diagnosis
    meter_filled = int(report.bds / 4)  # 25 characters max
    meter_empty = 25 - meter_filled
    color = c_green if report.bds < 15 else (c_yellow if report.bds < 35 else c_red)
    
    lines.append(f"{c_bold}BULLSHIT DENSITY SCORE (BDS):{c_reset} {color}{report.bds}%{c_reset} [{color}{'█' * meter_filled}{'░' * meter_empty}{c_reset}]")
    lines.append(f"{c_bold}DIAGNOSTIC STATUS:{c_reset} {color}{status}{c_reset}")
    lines.append(f"{c_bold}ANALYSIS:{c_reset} {diag}")
    lines.append(f"{c_bold}RECOMMENDED ACTION:{c_reset} {action}\n")

    # Category Breakdown
    if report.categories:
        lines.append(f"{c_bold}CONTAMINATION SOURCES:{c_reset}")
        for cat, count in sorted(report.categories.items(), key=lambda x: -x[1]):
            lines.append(f"  • {c_cyan}{cat}{c_reset}: {count} instance(s)")
        lines.append("")

    # Translation Log
    lines.append(f"{c_bold}--- DECODED SUBTEXT TRANSLATION ---{c_reset}")
    if not report.matches:
        lines.append(f"{c_green}✓ No corporate, academic, or performative bullshit detected.{c_reset}\n")
    else:
        for idx, m in enumerate(report.matches, 1):
            lines.append(f"\n{c_bold}[{idx}] DETECTED PHRASE:{c_reset} {c_red}\"{m.raw}\"{c_reset} {c_dim}(Category: {m.definition.category}){c_reset}")
            lines.append(f"    {c_bold}REALITY TRANSLATION:{c_reset} {c_green}→ \"{m.definition.translation}\"{c_reset}")
        lines.append("")

    lines.append(f"{c_bold}========================================================================{c_reset}")
    return "\n".join(lines)
