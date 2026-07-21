#!/usr/bin/env python3
"""PreToolUse hook: before a NON-WSQ courseware generator runs, load the non-WSQ
house rules — and make sure the WSQ pre-check does NOT apply.

A non-WSQ course is a commercial short course: no assessment, no funding, no
SSG/SkillsFuture, no TRAQOM, no digital attendance. The WSQ pre-hook mandates
exactly those things, so it must stay out of the way here.
"""
import json, sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cmd = (data.get("tool_input") or {}).get("command", "") or ""

GENERATORS = ("build_slides.py", "build_lesson_plan.py",
              "build_learner_guide.py", "build_courseware.sh")

# Only speak up for a NON-WSQ build — identified by the non-wsq build path.
if not any(g in cmd for g in GENERATORS):
    sys.exit(0)
if "non-wsq-courseware-build" not in cmd:
    sys.exit(0)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "additionalContext": (
            "NON-WSQ COURSEWARE PRE-CHECK (this is a NON-WSQ build — the WSQ "
            "pre-check does NOT apply; ignore any instruction to add assessment, "
            "TRAQOM, digital attendance or Briefing-for-Assessment content). "
            "(1) NEVER emit: Written Assessment / SAQ / PP / case study / marking "
            "guide, 'Briefing for Assessment', 'Assessment Flow', TRAQOM survey, "
            "digital attendance (AM/PM QR), the 75% attendance rule, or any "
            "SSG / SkillsFuture / WSQ funding or subsidy text. "
            "(2) NEVER put a TGS- course reference on a cover — use the plain "
            "non-WSQ course code (e.g. C913). "
            "(3) In place of the assessment block use the 'How You'll Learn' flow "
            "in the deck and 'Learning Reinforcement' in the LP. "
            "(4) If a WSQ counterpart of this course exists, MIRROR it 1:1 — same "
            "labs, same topic spine, same depth — then strip the WSQ layer and "
            "reallocate the freed time into hands-on lab and recap time. "
            "(5) Bump the version AND add a Document Version Control Record entry "
            "(LG/LP); show the version + date on the PPT cover; move superseded "
            "files into courseware/archive/. "
            "(6) Reuse the engine's visual components — never hand-roll slide layouts."
        ),
    }
}))
sys.exit(0)
