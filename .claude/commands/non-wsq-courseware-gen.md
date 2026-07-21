# non-wsq-courseware-gen

Use `non-wsq-courseware-build`. Generate the PPT, Learner Guide, Lesson Plan and connected labs, run the generator, then invoke `non-wsq-courseware-qa`. Never modify WSQ-prefixed or unprefixed shared tooling.

## Mirror the WSQ courseware when one exists

If the course has a **WSQ counterpart** (a `TGS-*` repo for the same subject),
mirror it rather than authoring from scratch. The non-WSQ course is the same
course minus the funding/compliance layer — it must not be a thinner course.

1. **Locate the WSQ source.** Look for a sibling `TGS-*` repo of the same
   subject (same course title / certification). If none exists, author normally
   from the course outline and skip the rest of this section.
2. **Mirror the structure 1:1** — the same labs (same count, same order, same
   titles), the same topic/domain spine, the same slide sections, the same LG
   depth and LP schedule shape, and the same `courseware/assets/`. Do not
   consolidate, drop or re-scope labs to make the course smaller.
3. **Then strip the WSQ layer.** Remove every funded-course element:

   | Strip | Replace with |
   |---|---|
   | Written Assessment, PP, case study, marking guides | nothing — non-WSQ has **no assessment** |
   | "Briefing for Assessment" + "Assessment Flow" slides | the **How You'll Learn** flow |
   | TRAQOM survey slides | nothing |
   | Digital attendance (AM/PM/Assessment QR) slides | nothing |
   | 75% attendance rule, funding/subsidy/SkillsFuture/SSG text | nothing |
   | `TGS-` course reference on covers | the plain non-WSQ code (e.g. `C913`) |
   | Assessment time in the LP schedule | reallocated to lab/practice time |

4. **Reallocate, don't shrink.** Time freed by removing assessment and admin
   blocks goes back into hands-on lab and recap time, so each training day
   still totals its full instructional hours.
5. **Verify with `non-wsq-courseware-qa`**, which fails the build on any leaked
   WSQ/SSG/TRAQOM/attendance/assessment content.
