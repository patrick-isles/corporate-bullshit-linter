"""
Unit tests for Corporate Bullshit Linter (CBL).
"""

import pytest
from cbl.engine import analyze_text

def test_clean_technical_text():
    raw = "The kernel driver crashed due to voltage droop. I patched GRUB with processor.max_cstate=1 and rebooted."
    report = analyze_text(raw)
    assert report.bds == 0.0
    assert len(report.matches) == 0
    assert report.diagnosis[0] == "CLEAN (0% BDS)"

def test_corporate_detection():
    raw = "Let's touch base and circle back so we can ensure alignment across all synergies."
    report = analyze_text(raw)
    assert report.bds > 20.0
    assert len(report.matches) == 4
    assert "Corporate Therapy-Speak" in report.categories

def test_academic_gatekeeping_detection():
    raw = "Our pedagogical framework relies on digital navigators to navigate logistical complications."
    report = analyze_text(raw)
    assert len(report.matches) == 3
    assert "Academic Gatekeeping" in report.categories
    assert any("digital navigators" in m.raw.lower() for m in report.matches)

def test_bourgeois_radicalism_detection():
    raw = "We are centering voices and raising awareness through revolutionary praxis."
    report = analyze_text(raw)
    assert len(report.matches) == 3
    assert "Bourgeois Radicalism" in report.categories
