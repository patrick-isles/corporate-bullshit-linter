"""
Corporate Bullshit Linter (CBL) - Command Line Interface.
"""

import sys
import argparse
import json
from .engine import analyze_text, render_terminal

DEMO_TEXT = """
Hi team,

I wanted to touch base regarding our strategic alignment. While we have low-hanging fruit,
our bandwidth is tight. Let's take this offline and circle back after we holding space
for stakeholder dialogue. The digital navigators ran into logistical complications,
so further review is required before we can unpack this.

Best,
Management
"""

def main():
    parser = argparse.ArgumentParser(
        prog="cbl",
        description="Corporate Bullshit Linter (CBL) - De-masking academic gatekeeping & corporate jargon.",
    )
    parser.add_argument("file", nargs="?", default=None, help="Text file to lint (reads from stdin if omitted).")
    parser.add_argument("--plain", action="store_true", help="Disable ANSI terminal colors.")
    parser.add_argument("--score-only", action="store_true", help="Output only the numeric Bullshit Density Score (0-100).")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output report in JSON format.")
    parser.add_argument("--demo", action="store_true", help="Run with built-in corporate/academic demo text.")
    parser.add_argument("--strict", action="store_true", help="Exit code 1 if BDS exceeds 15%% (Strict CI/CD mode).")

    args = parser.parse_args()

    # Input resolution
    if args.demo:
        input_text = DEMO_TEXT.strip()
    elif args.file and args.file != "-":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                input_text = f.read()
        except Exception as e:
            sys.stderr.write(f"[-] Error reading file: {e}\n")
            sys.exit(2)
    else:
        # Check if stdin has data
        if sys.stdin.isatty():
            # If no pipe and no file, show demo or help
            sys.stderr.write("[!] No input provided. Run 'cbl --help' or 'cbl --demo'\n")
            sys.exit(2)
        input_text = sys.stdin.read()

    report = analyze_text(input_text)

    if args.score_only:
        print(f"{report.bds}")
    elif args.as_json:
        data = {
            "bullshit_density_score": report.bds,
            "word_count": report.word_count,
            "matches_count": len(report.matches),
            "status": report.diagnosis[0],
            "diagnosis": report.diagnosis[1],
            "action": report.diagnosis[2],
            "categories": report.categories,
            "translations": [
                {
                    "phrase": m.raw,
                    "category": m.definition.category,
                    "translation": m.definition.translation,
                    "severity": m.definition.severity,
                }
                for m in report.matches
            ]
        }
        print(json.dumps(data, indent=2))
    else:
        print(render_terminal(report, plain=args.plain))

    # Exit code determination
    threshold = 15.0 if args.strict else 35.0
    sys.exit(1 if report.bds >= threshold else 0)

if __name__ == "__main__":
    main()
