# Patrick Winston MIT Presentation Master — Reference

> Single source of truth for the 5 frameworks distilled from Winston's
> "How To Speak" MIT lecture. All other Winston-derived artefacts in this
> repo (specs, rubrics, audits) MUST cite this file. To revise Winston
> guidance, edit this file first then propagate downward.

**Source:** `Patrcik Winston MIT Presentation Master/*.jpeg` (5 infographic cards from getintoai Instagram, distilling Winston's MIT lecture).

**Layer mapping:**

| Framework | Layer | Governs |
|-----------|-------|---------|
| F1 Start Right | DECK-LEVEL | `specs/presentation-design-spec.md` (opening slide & first 60s) |
| F2 Slide Crimes | SLIDE-LEVEL | `rubrics/_template.md` (per-slide checklist) |
| F3 STAR (Unforgettable) | DECK-LEVEL | `specs/presentation-design-spec.md` (deck core idea) |
| F4 Persuade Structure | DECK-LEVEL | `specs/presentation-design-spec.md` (32-slide architecture) |
| F5 Props & Stories | SLIDE-LEVEL | `rubrics/_template.md` (trigger for INDF case + difficult concept slides) |

**Phase mapping (CLAUDE.md):**

| Framework | Phase 1 (brainstorm) | Phase 3 (plan) | Phase 4 (build) | Phase 4 (review) |
|-----------|----------------------|----------------|-----------------|-------------------|
| F1 | input | required output | applied to slide 1 | gate |
| F2 | (n/a) | rubric items | applied per slide | gate |
| F3 | input | required output | applied throughout | gate |
| F4 | input | required output | block boundaries | gate |
| F5 | input | required output | case+concept slides | gate |

---

## F1 — START ANY PRESENTATION RIGHT [DECK-LEVEL]

**Prompt role:** Act as a presentation coach applying Patrick Winston's
MIT framework — every talk must open with an empowerment promise that
tells the audience exactly what they will know by the end that they
didn't know at the beginning.

**Task:** Write a powerful opening for my presentation that makes the audience immediately
understand why staying is worth every minute of their time.

**Steps:**
1. Ask for my presentation topic, audience, and desired outcome before starting
2. Identify the single most valuable thing my audience will walk away knowing
3. Write the empowerment promise — specific, outcome-driven, impossible to ignore
4. Design the first 60 seconds — promise, context, and why this matters now
5. Flag everything that should be cut from the opening — jokes, thank yous, apologies

**Rules:**
- Never open with a joke — audience isn't ready
- Never open with "thank you for having me" — weak and forgettable
- Empowerment promise must be specific — not "you'll learn about X" but "by the end you'll be able to do Y"
- First 60 seconds must earn the next 60 minutes
- Cut everything that doesn't serve the promise

**Output chain:** Empowerment Promise → First 60 Seconds → What to Cut → Opening Script

---

## F2 — ELIMINATE YOUR SLIDE CRIMES [SLIDE-LEVEL]

**Prompt role:** Act as a slide crime investigator applying Patrick
Winston's MIT framework — every presentation crime that puts audiences
to sleep gets identified, prosecuted, and eliminated.

**Task:** Audit my presentation slides and eliminate every crime Winston identified that
makes audiences disengage, sleep, or leave mentally.

**The 10 Slide Crimes:**
1. Too many slides
2. Too many words per slide
3. Font size under 40pt
4. Reading slides aloud *(DELIVERY CRIME — not auditable from file)*
5. Laser pointer usage *(DELIVERY CRIME)*
6. Speaker standing far from slides *(DELIVERY CRIME)*
7. No white space or air
8. Background clutter and logos
9. Collaborators list as final slide
10. "Thank you" or "Questions?" as final slide

**Steps:**
1. Ask me to describe or share my current slides before starting
2. Check for the 10 Winston slide crimes
3. Flag every crime with a specific fix
4. Redesign the final slide as a contributions slide
5. Deliver a clean slide brief — what stays, what goes, what changes

**Rules:**
- Every crime must have a specific fix — not just a flag
- Font minimum 40pt — no exceptions
- Final slide must be contributions — never questions or thank you
- White space is not wasted space — it's breathing room for the audience's brain
- Slides are condiments — not the main event

**Output chain:** Crime Audit → Fix per Crime → Final Slide Redesign → Clean Slide Brief

**Audit separation per spec E2:** Crimes #4, #5, #6 are delivery crimes (only auditable during live presentation). They go to `delivery-checklist.md`, not `crime-inventory.md`.

---

## F3 — MAKE YOUR IDEAS UNFORGETTABLE (STAR) [DECK-LEVEL]

**Prompt role:** Act as a personal brand architect applying Winston's Star
framework — Symbol, Slogan, Surprise, Salient idea, Story — to make any
idea impossible to forget.

**Task:** Apply Winston's Star to my core idea so it sticks in every
audience's mind long after the presentation ends.

**Steps:**
1. Ask for my core idea, audience, and what I want them to remember before starting
2. Design the Symbol — a visual or object that represents the idea instantly
3. Write the Slogan — a short phrase that becomes the handle people use to remember it
4. Identify the Surprise — the counterintuitive truth that makes people stop and think
5. Sharpen the Salient idea — the one idea that sticks out above everything else
6. Build the Story — how it works, why it matters, and the journey that led here

**Rules:**
- Symbol must be visual and specific — not abstract
- Slogan must be repeatable in a meeting without explanation
- Surprise must genuinely challenge an assumption — not just be interesting
- Salient idea must be one — never two or three
- Story must be personal enough to be specific, universal enough to resonate

**Output chain:** Symbol → Slogan → Surprise → Salient Idea → Story → Winston Star Summary

**Indonesian adaptation per spec E5:** Slogan diuji dalam Bahasa Indonesia. Bagian English disertakan di catatan kaki untuk traceability.

---

## F4 — STRUCTURE ANY TALK THAT PERSUADES [DECK-LEVEL]

**Prompt role:** Act as a persuasion architect applying Winston's job talk
framework — vision, proof of work, and contributions — to any presentation
that needs to convince, convert, or close.

**Task:** Structure my talk so the audience knows my vision, believes I've done
something significant, and remembers exactly what I contributed — all within
the first 5 minutes.

**Steps:**
1. Ask for my presentation goal, audience, and what I want them to do after before starting
2. Build the vision statement — the problem someone cares about and my new approach
3. Design the proof of work — the steps taken that prove I've done something real
4. Structure the 5-minute opening that establishes both vision and credibility
5. Build the contributions close — the final slide that mirrors the opening promise

**Rules:**
- Vision must be established within 5 minutes — never later
- Proof of work must be specific steps — not vague accomplishments
- Opening and close must mirror each other — promise made, promise kept
- Contributions slide stays up during questions — never replaced with "thank you"
- Every minute must advance either vision or proof — nothing else

**Output chain:** Vision Statement → Proof of Work → 5-Minute Opening → Contributions Close → Full Talk Structure

---

## F5 — USE PROPS AND STORIES TO TEACH ANYTHING [SLIDE-LEVEL]

**Prompt role:** Act as a teaching design specialist applying Winston's
prop and storytelling frameworks — the techniques that make ideas feel
physical, memorable, and impossible to misunderstand.

**Task:** Design a prop or story that makes my most complex idea feel as
simple and physical as holding it in your hands.

**Steps:**
1. Ask for the complex idea I need to teach and my audience before starting
2. Identify the single most confusing aspect of the idea
3. Design a physical prop or demonstration that makes the confusion disappear
4. Build a story around the prop — tension, demonstration, resolution
5. Write the verbal script that guides the audience from confusion to clarity

**Rules:**
- Prop must be physical and demonstrable — not a slide or diagram
- Story must have genuine tension before the resolution
- Script must guide attention — tell them where to look and what to notice
- Demonstration must work even if it fails — the failure itself teaches
- If no physical prop exists, design the closest verbal equivalent

**Output chain:** Confusing Concept → Prop Design → Story Arc → Verbal Script → Teaching Sequence

**Adaptation for INDF case slides per spec E3:** Numbers are the prop. Required story arc: konteks/ketegangan → demonstrasi (tabel/grafik) → resolusi (interpretasi via FASB).
