"""
Corporate Bullshit Linter (CBL) Package.
"""

from .engine import analyze_text, render_terminal, LintReport
from .dictionary import LEXICON

__version__ = "1.0.0"
__all__ = ["analyze_text", "render_terminal", "LintReport", "LEXICON"]
