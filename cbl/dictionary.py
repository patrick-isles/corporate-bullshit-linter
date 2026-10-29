"""
Corporate Bullshit Linter (CBL) - Lexicon of Bureaucratic & Performative Deceptions.
Categorized translations from academic gatekeeping, corporate therapy-speak, and faux-radical posturing.
"""

from typing import Dict, NamedTuple

class BSDefinition(NamedTuple):
    translation: str
    category: str
    severity: int  # 1 to 5 scale

LEXICON: Dict[str, BSDefinition] = {
    # =========================================================================
    # 1. ACADEMIC GATEKEEPING & BUREAUCRATIC INERTIA
    # =========================================================================
    r"\bpedagogical framework\b": BSDefinition(
        "arbitrary assignment rubrics made up a decade ago", "Academic Gatekeeping", 4
    ),
    r"\bdigital navigators?\b": BSDefinition(
        "salaried administrators paid to ignore emails", "Academic Gatekeeping", 5
    ),
    r"\bprerequisite chain\b": BSDefinition(
        "tuition extortion funnel forcing you into basic algebra after Calc 2", "Academic Gatekeeping", 5
    ),
    r"\bacademic rigor\b": BSDefinition(
        "tedious busywork assigned to justify an adjunct's existence", "Academic Gatekeeping", 4
    ),
    r"\blearning outcomes?\b": BSDefinition(
        "check-box metrics for regional accreditation auditors", "Academic Gatekeeping", 3
    ),
    r"\boffice hours?\b": BSDefinition(
        "a 20-minute window where the professor hides with the door locked", "Academic Gatekeeping", 3
    ),
    r"\bsyllabus is a contract\b": BSDefinition(
        "rules enforced strictly on students while the instructor ignores accommodations", "Academic Gatekeeping", 5
    ),
    r"\blogistical complications?\b": BSDefinition(
        "an instructor refusing to open an email attachment", "Academic Gatekeeping", 5
    ),
    r"\bfurther review\b": BSDefinition(
        "hoping the student drops the course before administrative intervention", "Academic Gatekeeping", 4
    ),
    r"\bcollaborative group work\b": BSDefinition(
        "one person carries the project while three people watch TikTok", "Academic Gatekeeping", 4
    ),
    r"\bcanvas module\b": BSDefinition(
        "a disorganized landfill of broken external links and Comic Sans PDFs", "Academic Gatekeeping", 3
    ),

    # =========================================================================
    # 2. CORPORATE THERAPY-SPEAK & MANAGERIAL DODGES
    # =========================================================================
    r"\bcircle back\b": BSDefinition(
        "ignore this until everyone forgets it existed", "Corporate Therapy-Speak", 3
    ),
    r"\btouch base\b": BSDefinition(
        "waste 15 minutes of your life asking for an update already in Jira", "Corporate Therapy-Speak", 3
    ),
    r"\bbandwidth\b": BSDefinition(
        "willingness to endure unpaid overtime this week", "Corporate Therapy-Speak", 4
    ),
    r"\blow-hanging fruit\b": BSDefinition(
        "obvious baseline tasks nobody bothered doing for six months", "Corporate Therapy-Speak", 2
    ),
    r"\bsynerg(y|ies)\b": BSDefinition(
        "pointless cross-department meetings that could have been a bash script", "Corporate Therapy-Speak", 4
    ),
    r"\bdeep dive\b": BSDefinition(
        "spend 3 hours pretending to read an executive slide deck", "Corporate Therapy-Speak", 3
    ),
    r"\balignment\b": BSDefinition(
        "nodding in silence so the VP doesn't throw a tantrum", "Corporate Therapy-Speak", 4
    ),
    r"\bholding space\b": BSDefinition(
        "staring blankly into a Zoom camera while calculating your hourly rate", "Corporate Therapy-Speak", 5
    ),
    r"\btake this offline\b": BSDefinition(
        "shut up before you expose management's complete technical ignorance", "Corporate Therapy-Speak", 5
    ),
    r"\bhard stop\b": BSDefinition(
        "I am profoundly bored and closing my laptop right now", "Corporate Therapy-Speak", 2
    ),
    r"\bthought leader(s)?\b": BSDefinition(
        "unemployed person with an active Substack and zero GitHub commits", "Corporate Therapy-Speak", 5
    ),
    r"\bmove the needle\b": BSDefinition(
        "generate arbitrary KPI spikes to justify a director's quarterly bonus", "Corporate Therapy-Speak", 4
    ),
    r"\baction item(s)?\b": BSDefinition(
        "chores dumped on the person who spoke last", "Corporate Therapy-Speak", 2
    ),
    r"\bparadigm shift\b": BSDefinition(
        "marginal software update with an inflated PR budget", "Corporate Therapy-Speak", 3
    ),

    # =========================================================================
    # 3. BOURGEOIS RADICALISM & PERFORMATIVE MORALITY
    # =========================================================================
    r"\braising awareness\b": BSDefinition(
        "wearing an ironic pastel t-shirt while accomplishing zero material change", "Bourgeois Radicalism", 4
    ),
    r"\bcentering voices\b": BSDefinition(
        "unearned moral lecturing without doing actual manual labor", "Bourgeois Radicalism", 4
    ),
    r"\bholding accountability\b": BSDefinition(
        "posting a multi-slide Instagram carousel instead of fixing the problem", "Bourgeois Radicalism", 4
    ),
    r"\bunpack this\b": BSDefinition(
        "over-intellectualize a brutally simple mistake", "Bourgeois Radicalism", 3
    ),
    r"\bpraxis\b": BSDefinition(
        "arguing about Sartre at a coffee shop while relying on parental trust funds", "Bourgeois Radicalism", 5
    ),
    r"\blived experience(s)?\b": BSDefinition(
        "an unfalsifiable personal anecdote deployed to shut down empirical data", "Bourgeois Radicalism", 4
    ),
    r"\bspace for dialogue\b": BSDefinition(
        "an echo chamber where dissent triggers an HR escalation", "Bourgeois Radicalism", 4
    ),
}
