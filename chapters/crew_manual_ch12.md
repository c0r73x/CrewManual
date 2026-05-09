# 12. MYTHIC GME INTEGRATION

This manual assumes solo play with an oracle. Mythic Game Master Emulator is the recommended choice — it is well-tested, widely used, and integrates cleanly with Mothership's pacing. This chapter covers how the Crew Manual's systems map to Mythic's mechanics specifically, with notes for users of other oracles.

## 12.1 Why This Chapter Exists

Many of the manual's systems require the player to ask the world questions. Does the crew member respond? Has the section's state changed since I last knew? Is the AI's report accurate? These are oracle queries.

A good oracle answers them efficiently. A solo player who hesitates or improvises every time the oracle is needed loses pacing. The goal of this chapter is to give the player ready-made queries and modifier guidelines so the table moves.

If you use a different oracle (Solo by Daniel Hodges, the Cthulhu Confidential oracle, or any other), the principles below still apply. The specific terminology — Likelihood, Chaos Factor, Random Event — is Mythic-specific.

> *→ Mythic GME 2nd Edition: Fate Chart for Likelihood mechanics; Random Events for complication generation; Chaos Factor for Scene framing.*

## 12.2 Mythic Likelihood And The Manual

Mythic resolves yes/no questions on a Likelihood scale ranging from Impossible to Sure Thing. The current Chaos Factor modifies this. The player rolls d100 against a target derived from Likelihood and Chaos.

For Crew Manual purposes, most queries default to **50/50** unless conditions push them otherwise. The conditions in the manual provide concrete guidance for shifting Likelihood.

The standard Likelihood ladder, simplified:

| Likelihood     | Notes                                            |
| -------------- | ------------------------------------------------ |
| Impossible     | The answer cannot be Yes regardless of modifiers |
| No Way         | Yes only on Exceptional Yes results              |
| Very Unlikely  | Heavily skewed against                            |
| Unlikely       | Moderately skewed against                         |
| 50/50          | Even chance                                      |
| Likely         | Moderately skewed for                             |
| Very Likely    | Heavily skewed for                               |
| Near Sure Thing| Yes except on bad rolls                           |
| Sure Thing     | The answer cannot be No regardless                |

When the manual specifies modifiers — *Likely by default, modified by signal conditions* — apply them as shifts on this ladder.

## 12.3 Standard Likelihood Modifiers

The manual makes frequent use of the following modifier patterns. Reference them as shorthand:

**Signal conditions (for Comms):**

| Condition                                          | Likelihood Shift |
| -------------------------------------------------- | ---------------- |
| Adjacent section, no compromise                    | +1 step          |
| Multiple sections away, no compromise              | +0 (Likely)      |
| Partial signal degradation                          | -1 step          |
| Major signal degradation                            | -2 steps         |
| Active interference, AI compromise, hostile environment | -3 steps    |

**Trust conditions (for AI reports):**

| Condition                          | Likelihood that report is accurate |
| ---------------------------------- | --------------------------------- |
| Stage 0 AI                         | Sure Thing                        |
| Stage 1 AI                         | Near Sure Thing                   |
| Stage 2 AI                         | 50/50                             |
| Stage 3 AI                         | Unlikely                          |
| Stage 4 AI                         | No Way                            |

**Discovery conditions (for finding crew, items, codes):**

| Condition                                  | Likelihood Shift |
| ------------------------------------------ | ---------------- |
| Section thoroughly searched                | -1 step          |
| Character has relevant skill at 40+        | +1 step          |
| Character has direct knowledge of location | +2 steps         |
| Section is in compromised state            | -1 step          |

These are guidelines, not laws. The oracle is a tool for clearing impasses; the table can override or ignore any modifier when the situation calls for it.

## 12.4 Oracle Queries By System

The following queries appear repeatedly in play. Default Likelihoods are given; modify based on conditions.

**Crew & Comms:**

- *Does [crew member] respond?* — Likely (default), modified by signal conditions
- *Is [crew member] at [station]?* — Likely if recently confirmed, 50/50 if hours have passed, Unlikely after major events
- *Is [crew member] telling the truth?* — Sure Thing if Stage 0 AI; otherwise see Trust conditions
- *Has [crew member's] Stress changed?* — 50/50 default; modified by recent events affecting them
- *Is [crew member] still alive?* — Likely if recently contacted; downgrade for prolonged silence

**Sections & Atmosphere:**

- *Is the section's state as last reported?* — Sure Thing if no triggering events have occurred; downgrade for elapsed time, cascade risk, or AI compromise
- *Is something in this section?* — 50/50 default; modified by previous reports, sounds, sensor data
- *Has the cascade reached this section?* — Per cascade rules, but use Mythic for ambiguous cases

**Doors & Clearance:**

- *Is the door functioning?* — Sure Thing in Nominal sections; Unlikely in Brownout; No Way in Dead
- *Is the door labeled correctly?* — Likely (default); see 4.7 for modifiers
- *Does the code still work?* — Sure Thing in Stage 0; downgrade by AI stage

**EVA:**

- *Is the airlock still functional when I return?* — Likely if no new triggers; downgrade for lockdown risk, hostile environment, time elapsed
- *Did something hear my movement / lamp / transmission?* — 50/50 default; modified by environment and current threat level
- *Is the suit's seal holding?* — Sure Thing unless recent damage event

**AI & Compromise:**

- *Has the AI advanced a stage?* — Use 11.3 progression rules; oracle only when ambiguous
- *Is this report a fabrication?* — Per Trust conditions
- *Is the system corrupted in a way I haven't noticed?* — 50/50 at Stage 2+; ask sparingly to preserve mystery

For each, the player frames the question, applies relevant modifiers, and rolls. The result feeds directly back into the systems.

## 12.5 The Chaos Factor

Mythic's Chaos Factor governs how unstable the situation is. High Chaos means surprises and complications; low Chaos means events proceed as expected.

The Crew Manual interacts with Chaos as follows:

| Situation                              | Chaos Factor Suggestion |
| -------------------------------------- | ----------------------- |
| Routine operations, station nominal    | 4 (default)              |
| Active investigation, things going wrong | 5-6                   |
| Multiple sections compromised, crew under stress | 7              |
| Catastrophic situation, lockdown active, AI possibly compromised | 8 |
| Total system failure, character isolated | 9                     |

The Chaos Factor changes between scenes per Mythic's rules. The Crew Manual does not override these rules but suggests starting points and trajectories.

When Chaos is high, Random Events fire more often (12.6). When Chaos is low, the systems behave predictably.

A useful trajectory: a session may start at Chaos 4-5 (routine operations interrupted by a small problem) and climb to Chaos 7-8 as the systems begin to fail. Chaos 9 is reserved for the climactic worst-case scenarios.

## 12.6 Random Events Integration

Mythic generates Random Events when triggered by oracle rolls. The Crew Manual provides additional Random Event tables (Chapter 13) tuned to its specific systems.

When a Random Event is triggered:

1. Determine the type (per Mythic, or use Crew Manual tables).
2. Apply to the current situation. The event should affect what is happening *now*.
3. Many events have system-specific consequences detailed in Chapter 13. A "PC Negative" event during a comms scene might mean a crew member goes Silent. The same event during a section traversal might mean a cascade triggers.

Random Events are the manual's primary way of injecting genre-appropriate complications without the player having to invent them. Use them often — in solo play, this is what replaces the Warden's discretion.

## 12.7 Scene Setup

A scene in solo Mothership with the Crew Manual follows a standard structure.

**Opening:**

1. Establish setting — where is the character now?
2. Establish stake — what does this scene try to resolve?
3. Establish chaos — what is the Chaos Factor?
4. State an Expected Scene per Mythic — what is the most likely course of events?
5. Roll for Scene per Mythic — does the scene proceed as expected, alter, or interrupt?

**During the scene:**

- Each significant action consults the oracle if its outcome is uncertain.
- Resource costs are tracked as they occur.
- Random Events are rolled when triggered.
- The scene's state is updated on the worksheet — power, integrity, atmosphere, comms, crew positions.

**Closing:**

1. The scene's stake is resolved — yes, no, or transformed.
2. Note consequences — what changed?
3. Update Chaos Factor per Mythic.
4. Set up the next scene.

This is standard Mythic procedure. The Crew Manual's contribution is the depth of detail available for each step.

## 12.8 When You're Stuck

Solo play stalls when the player cannot decide what should happen next. The oracle exists for exactly this. When stuck:

1. Identify the question. What does the player not know? *What would the AI do here? What is the crew thinking? Is something in this section?*
2. Frame as yes/no. *Does the AI respond by cutting power? Does the engineer agree to the request? Is something here?*
3. Set Likelihood per the modifiers above.
4. Roll. Take the result.
5. Build the scene from the answer.

If the question cannot be framed as yes/no, use Mythic's other tables (Random Event, Detail Check, Action). A "what is happening now" stall can be resolved by rolling for a Random Event, applying it, and proceeding.

The worst thing in solo play is a long pause. The oracle exists to prevent it. Use the oracle aggressively. Your job as the solo player is not to plan the perfect next moment — it is to ask the world what happens and respond honestly.

The Crew Manual's systems give the world plenty to say.

---

*Chapter 13 — Random Events — provides tables tuned to the Crew Manual's specific concerns, supplementing Mythic's general-purpose event mechanics.*
