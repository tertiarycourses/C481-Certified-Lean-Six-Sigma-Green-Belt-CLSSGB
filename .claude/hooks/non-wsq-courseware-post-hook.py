#!/usr/bin/env python3
"""PostToolUse hook: after a NON-WSQ courseware generator runs, require the
non-WSQ QA audit and restate what must NOT have leaked into the artifacts.

Course-agnostic: it never hardcodes a course's filenames. The build engine
derives outputs from course_data.SHORT_TITLE, so QA resolves them the same way.
"""
import json, sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cmd = (data.get("tool_input") or {}).get("command", "") or ""

GENERATORS = ("build_slides.py", "build_lesson_plan.py",
              "build_learner_guide.py", "build_courseware.sh")

if not any(g in cmd for g in GENERATORS):
    sys.exit(0)
if "non-wsq-courseware-build" not in cmd:
    sys.exit(0)

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": (
            "NON-WSQ COURSEWARE POST-CHECK (mandatory): non-WSQ courseware was "
            "just (re)generated. This is NOT a WSQ build — do not apply the WSQ "
            "post-check (no TRAQOM, no Assessment Flow, no Briefing-before-"
            "Assessment, no trainer-profile/practice-exam mandates). Instead: "
            "(1) Run /non-wsq-courseware-qa (or the non-wsq-courseware-qa agent) "
            "and RENDER the changed pages to images to verify them. "
            "(2) FAIL the build on any leaked WSQ content: SSG, SkillsFuture, WSQ, "
            "TRAQOM, funding/subsidy, digital attendance, 75% attendance rule, "
            "TGS- reference, or ANY assessment/marking/SAQ/PP/case-study content. "
            "(3) Verify PPT, LP and LG all exist, are non-trivial in size, and "
            "agree with each other on course code, title, version and lab count "
            "(the single-source guarantee). "
            "(4) Verify the cover shows ONE version matching the filename, the "
            "Document Version Control Record has a row for it, and superseded "
            "versions were moved to courseware/archive/. "
            "(5) Check for overlapping, clipped or overflowing text on rendered "
            "pages. Fix, regenerate, and re-run until it passes."
        ),
    }
}))
sys.exit(0)
