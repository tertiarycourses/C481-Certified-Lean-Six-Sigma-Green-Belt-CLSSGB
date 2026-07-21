"""
SINGLE SOURCE OF TRUTH — C481 Certified Lean Six Sigma Green Belt (CLSSGB).

This is the NON-WSQ edition of the Certified Lean Six Sigma Green Belt course.
It MIRRORS the WSQ course (TGS-2025055775) 1:1 — the same DMAIC spine, the same
25 labs, the same Green Belt statistical depth — with the entire WSQ funding and
compliance layer stripped out.

Content is grounded in:
  * The original trainer deck's teaching diagrams, imported into
    courseware/assets/diagrams/ and shown verbatim so formulas are reproduced
    exactly as the trainer taught them.
  * "Six Sigma: A Complete Step-by-Step Guide" — The Council for Six Sigma
    Certification (CSSC), July 2018 edition. The CSSC scopes the belts by
    chapter: Yellow Belt = Ch 1-11, GREEN BELT = Ch 1-24. Everything in
    Ch 12-24 (MSA/Gage R&R, distributions, correlation & regression, hypothesis
    testing, sample size, control charts, capability) is therefore Green-Belt
    material and is taught here in depth.

WHAT WAS STRIPPED (and must never be reintroduced)
--------------------------------------------------
  * The TSC alignment block and every competency code in the learning outcomes
    and lab objectives.
  * The final graded papers — there is NO graded instrument in a non-WSQ course;
    learning is reinforced through the labs and the improvement package.
  * TRAQOM, digital attendance (AM/PM QR), the 75% attendance rule, and all
    SSG / SkillsFuture / funding text.
  * The TGS- course reference — this course carries the plain code C481.

The Day 4 time formerly spent on the final papers (165 minutes) is reallocated
to hands-on lab, consolidation and recap time. The course is not shortened.

STEP UP FROM YELLOW BELT
------------------------
The Yellow Belt supports a project; the Green Belt LEADS one and owns the
statistics. Every DMAIC phase below therefore carries the Yellow Belt tool PLUS
its Green Belt statistical counterpart:
    Define   : charter -> + Kano, affinity, CTQ trees, stakeholder/RACI
    Measure  : check sheet -> + MSA/Gage R&R, sampling theory, sample size, capability
    Analyze  : 5 Whys/Pareto -> + hypothesis testing, p-values, correlation, regression
    Improve  : brainstorm -> + solution selection matrix, FMEA/RPN, DOE, piloting
    Control  : control plan -> + SPC, control chart selection, Cp/Cpk, out-of-control rules

Every artifact (PPT, LP, LG, LG.md, labs index) is generated from this
module + data_domainN.py so they stay 100% aligned.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Certified Lean Six Sigma Green Belt (CLSSGB)"
SHORT_TITLE  = "Certified Lean Six Sigma Green Belt (CLSSGB)"
COURSE_CODE  = "C481"                      # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "21 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 4

# ------------------------------------------------------------------ outcomes
# Mirrors the WSQ outcomes with the competency codes removed.
LEARNING_OUTCOMES = [
    "LO1: Lead a Lean Six Sigma project — define the problem, scope the work and charter the project.",
    "LO2: Map and baseline a process using SIPOC, detailed process maps and value stream maps.",
    "LO3: Build a valid measurement system — sampling, sample size and MSA/Gage R&R — and baseline capability.",
    "LO4: Analyse process data statistically using Pareto, run charts, hypothesis testing, correlation and regression.",
    "LO5: Identify and prove root causes of variation using Fishbone, 5 Whys and statistical evidence.",
    "LO6: Select, risk-assess and pilot improvements using solution selection matrices, FMEA and DOE.",
    "LO7: Sustain the gain with SPC control charts, process capability and a control plan.",
]

# ------------------------------------------------------------------ topics
# The course follows the DMAIC roadmap end to end. Foundations establish the
# language and the Y = f(X) model, then one topic per DMAIC phase. Every lab
# lands inside the phase it belongs to, so slides, LG, LP and labs tell one story.
TOPICS = [
    dict(num=0, code="00", phase="FOUNDATIONS",
         title="Six Sigma Foundations & The Green Belt Role",
         subtitle="Quality · Lean · Six Sigma · Y = f(X) · Belt roles · COPQ · Project selection · DMAIC",
         weighting="10%",
         concepts=[
            ("What is Quality", "Conformance to customer requirements — the customer sets the standard, not the producer."),
            ("Lean vs Six Sigma", "Lean attacks waste and speed; Six Sigma attacks variation and defects. Together: fast AND consistent."),
            ("Y = f(X)", "The output Y is a function of the process inputs Xs. Improve Y by finding and controlling the vital few Xs."),
            ("Sigma level & DPMO", "Six Sigma = 3.4 defects per million opportunities, including the 1.5 sigma long-term shift."),
            ("Cost of Poor Quality", "The visible defect cost is the tip of the iceberg — rework, delay and lost custom sit below the waterline."),
            ("The Green Belt role", "The Green Belt LEADS a scoped DMAIC project and owns the data analysis, supported by a Black Belt."),
            ("Project selection", "A good project has a real gap, available data, a manageable scope and a business sponsor."),
            ("The DMAIC roadmap", "Define, Measure, Analyze, Improve, Control — with a tollgate review at the end of each phase."),
         ]),
    dict(num=1, code="D", phase="DEFINE",
         title="Define — Scope the Problem",
         subtitle="VOC · CTQ trees · Kano · Affinity · Charter · Problem statement · SIPOC · Stakeholders",
         weighting="18%",
         concepts=[
            ("Voice of the Customer", "Capture what the customer actually says — reactive and proactive sources — before deciding anything."),
            ("Affinity diagram", "Cluster raw VOC statements into natural themes so the signal emerges from the noise."),
            ("Kano analysis", "Classify requirements as Must-Be, One-Dimensional or Delighter — they are not equally valuable."),
            ("CTQ tree", "Translate each need into a specific, measurable Critical-to-Quality requirement with a target and limits."),
            ("Project charter", "Problem, goal, scope, business case, team and timeline — the project's contract with the sponsor."),
            ("Problem statement", "Process, time period, measurable gap and impact — and never a cause or a solution."),
            ("SIPOC", "The macro as-is map: Suppliers, Inputs, Process, Outputs, Customers — agree the boundaries first."),
            ("Stakeholders & RACI", "Name who is Responsible, Accountable, Consulted and Informed before the project starts."),
         ]),
    dict(num=2, code="M", phase="MEASURE",
         title="Measure — Quantify Performance",
         subtitle="Process mapping · VSM · Takt · Data types · Sampling · Sample size · MSA/Gage R&R · Yield · DPMO · Baseline capability",
         weighting="24%",
         concepts=[
            ("Process mapping", "Flowcharts and swimlanes expose the handoffs, delays and rework loops where defects are born."),
            ("Value stream mapping", "Map material AND information flow, then compare value-added time against total lead time."),
            ("Lean metrics", "WIP, lead time, cycle time, throughput and takt time — takt = available time / customer demand."),
            ("Types of data", "Continuous vs discrete; nominal vs ordinal. The data type dictates which statistical tool is legal."),
            ("Sampling", "Simple random, stratified, systematic and cluster — a biased sample invalidates every later conclusion."),
            ("Sample size", "n = (1.96s/d)^2 for continuous data — how much data is enough, decided before you collect it."),
            ("MSA / Gage R&R", "Before trusting the data, prove the measurement system: accuracy, repeatability, reproducibility."),
            ("Yield, DPU, DPO, DPMO", "Classic yield hides rework; first pass and rolled throughput yield expose the hidden factory."),
            ("Baseline capability", "Convert the baseline into a sigma level and Cp/Cpk so improvement can be proven later."),
         ]),
    dict(num=3, code="A", phase="ANALYZE",
         title="Analyze — Find and Prove the Root Cause",
         subtitle="Variation · Pareto · Run charts · Fishbone · 5 Whys · Multi-voting · Hypothesis testing · p-values · Correlation · Regression",
         weighting="26%",
         concepts=[
            ("Common vs special cause", "Common cause is built into the process; special cause is an external, assignable signal."),
            ("Pareto analysis", "The 80/20 rule separates the vital few causes from the trivial many — attack the vital few."),
            ("Run charts", "Plot the metric over time to reveal trend, shift, cluster, mixture, oscillation and bias."),
            ("Fishbone (Ishikawa)", "Organise candidate causes by 5M+E — Manpower, Method, Machine, Material, Measurement, Environment."),
            ("5 Whys", "Drill from the symptom to an actionable cause — stop when the answer is a process, not a person."),
            ("Descriptive statistics", "Central tendency (mean, median) and dispersion (range, standard deviation) describe the data."),
            ("Hypothesis testing", "State H0 and Ha, choose the right test, then let the p-value decide — not the loudest voice."),
            ("p-value & alpha", "If p < alpha, reject H0. At 95% confidence alpha = 0.05. Type I risks the producer, Type II the consumer."),
            ("Correlation & regression", "Quantify how strongly an X drives Y — and remember correlation never proves causation."),
         ]),
    dict(num=4, code="I", phase="IMPROVE",
         title="Improve — Select, De-Risk and Pilot the Fix",
         subtitle="Solution generation · Benchmarking · Solution selection matrix · 5S · Poka-Yoke · Pull/JIT · FMEA · DOE · Piloting",
         weighting="12%",
         concepts=[
            ("Generating solutions", "Brainstorming, brainwriting, six thinking hats and anti-brainstorming — diverge before converging."),
            ("Benchmarking", "Learn from who already does it best, inside or outside your industry."),
            ("Solution selection matrix", "Score candidate solutions against weighted criteria — feasibility, cost, impact and time."),
            ("5S & visual workplace", "Sort, Set in order, Shine, Standardise, Sustain — for physical and digital work alike."),
            ("Poka-Yoke", "Mistake proofing makes the error difficult, obvious or impossible in the first place."),
            ("Pull, JIT & Heijunka", "Let demand pull the work, level the load, and stop pushing inventory into the process."),
            ("FMEA & RPN", "Severity x Occurrence x Detection = RPN — de-risk the change before it goes live."),
            ("Design of Experiments", "Vary factors together, not one at a time, so interactions between Xs become visible."),
            ("Piloting", "Test at small scale, measure against the baseline, then decide to scale, adjust or stop."),
         ]),
    dict(num=5, code="C", phase="CONTROL",
         title="Control — Hold the Gain",
         subtitle="SPC · Control chart selection · Control limits · Out-of-control rules · Cp/Cpk · Control plan · SOP · Visual management · Handover",
         weighting="10%",
         concepts=[
            ("Statistical Process Control", "Monitor the process with data over time so drift is caught before it becomes a defect."),
            ("Control chart anatomy", "Centre line plus upper and lower control limits at +/- 3 standard deviations."),
            ("Control chart selection", "Continuous or attribute? Subgroup size? That decides Xbar-R, Xbar-S, I-MR, p, np, c or u."),
            ("Out-of-control rules", "A point beyond 3 sigma, runs, trends and hugging patterns each signal a special cause."),
            ("Control limits vs spec limits", "Control limits come from the process voice; specification limits come from the customer."),
            ("Cp and Cpk", "Cp = spec width / process spread. Cpk also accounts for centring — aim for Cpk >= 1.33."),
            ("Control plan", "Metric, target, measurement method, frequency, owner and the reaction plan when it drifts."),
            ("Standard work & SOP", "Lock the improved method into written, trainable, auditable standard work."),
            ("Handover & closure", "Transfer ownership to the process owner, verify the benefit, then formally close the project."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Six Sigma foundations, the Green Belt role and the Define phase",
    2: "Measure — process mapping, sampling, MSA and baseline capability",
    3: "Analyze — root cause, hypothesis testing, correlation and regression",
    4: "Improve, Control and consolidating your improvement package",
}
