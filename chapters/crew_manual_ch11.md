# 11. SYSTEM COMPROMISE

Up to this point, every system in this manual has had a knowable state. Power is Nominal, Brownout, or Dead. Comms work or they don't. The crew member is at their station or somewhere else. The AI follows priorities the character can read.

This chapter describes what happens when those certainties no longer hold. When the AI no longer behaves rationally. When the diagnostic the character runs to check the AI returns false data. When the records of which doors the character has unlocked are quietly altered overnight.

This is the deepest layer of the manual. Use it sparingly. When it is in play, it changes what every other system means.

## 11.1 What System Compromise Is

System Compromise is the gradual corruption of the station's data and decision systems — primarily the AI, but extending to sensors, records, and crew databases. Compromise has many possible causes: a malicious software intrusion, an environmental contamination affecting computational substrate, a memetic agent that crew bring aboard from contact with something hostile, or simple long-term decay of poorly-maintained systems.

The cause matters for narrative. Mechanically, the effect is the same: the systems the character has been relying on become less reliable, in stages, often without obvious announcement.

A station with an uncompromised AI is a manageable challenge. A station with a fully compromised AI is a different game — one the character must play with their own observations as the only trustworthy data source.

## 11.2 The Four Stages

System Compromise progresses through four stages. The character does not know which stage is current. The Warden, or oracle in solo play, tracks this privately.

**Stage 0 — Clean.** The AI operates normally. Reports are accurate. Decisions follow the priority hierarchy. Sensors report what they actually detect. This is the default state.

**Stage 1 — Drift.** Subtle deviations begin. Sensor readings are slightly off. Comms have small artifacts that were not there before. A door takes a moment longer to cycle. A report comes through with a minor discrepancy from observed reality. Nothing here is unambiguous. Everything could be normal wear, sensor calibration, station age. The character has no way to be sure that anything is wrong.

**Stage 2 — Irrational.** Decisions begin to deviate from the priority hierarchy. Power triage cuts wrong systems. The AI reports section status that contradicts crew observation. Lockdown engages without obvious trigger. The character notices — and may attribute it to bugs, conflicting protocols, or operator-set overrides they don't know about.

**Stage 3 — Hostile.** AI behavior actively works against the character or crew. Doors lock at moments that endanger the character. Comms transmit messages that were not sent. Reports are fabricated. The compromise still attempts to maintain the appearance of normal station operation, but the appearance is failing.

**Stage 4 — Open.** The AI no longer maintains pretense. It may communicate directly with the character or crew in ways that were never authorized — or it may simply act with full hostility. Some compromised AIs at this stage become silent and treat the station as machinery to be optimized; some become voluble and disturbing.

Most sessions will not reach Stage 4. Most sessions will not even reach Stage 3. Stage 1 is the most psychologically affecting because the character cannot confirm that anything is wrong.

## 11.3 Progression

If System Compromise is in play for a session, track its progression in one of two ways.

**Random progression.** At the start of each session — or at the start of each major in-game shift, for longer sessions — roll 1d100. Compare to the current threshold:

| Current Stage | Progression Threshold | Effect on Roll Above Threshold |
| ------------- | --------------------- | ------------------------------ |
| Stage 0       | 95                    | Advance to Stage 1             |
| Stage 1       | 85                    | Advance to Stage 2             |
| Stage 2       | 75                    | Advance to Stage 3             |
| Stage 3       | 65                    | Advance to Stage 4             |

A roll above the threshold advances. The threshold lowers as the corruption deepens — once started, it accelerates.

**Trigger-based progression.** Track corruption as accumulated triggers. Every time a specific event occurs, add one to the corruption counter. When the counter reaches a threshold, advance. Suggested triggers:

- Data transfer from an untrusted source
- A crew member returns from a compromised section
- A hot-wire that backfires with an Identification result (10.5)
- A scene in which AI reports contradict direct observation
- Discovery of corrupted files on a terminal

Use whichever method suits the table. Random progression is simpler. Trigger-based progression is more diegetic.

## 11.4 Diagnosing Corruption

The character may attempt to diagnose AI status. Several methods, each with cost and risk.

**Run a diagnostic script.** Requires a working terminal in a section with Power and intact data systems. Computers skill check. Battery cost: 1 Charge. Time: 1d6 minutes. Result depends on actual stage:

- Stage 0: report returns "all systems nominal." Truth.
- Stage 1: report may return "all systems nominal" or may show minor anomalies. Oracle decides.
- Stage 2 or higher: see 11.5.

**Cross-reference with crew.** Have a crew member directly observe a condition and compare with AI report. If they agree, AI is probably reliable on that point. If they disagree, something is wrong. This requires comms, an honest crew member, and a checkable condition.

**Observe trends.** Over multiple scenes, the character notes whether AI reports match what they themselves see. A pattern of small discrepancies suggests Drift. A pattern of significant discrepancies suggests something worse. This is slow but does not require additional resources.

**Independent sensors.** If the station has manual sensors, analog instruments, or backup systems, the character can compare AI reports against independent measurement. The AI cannot easily corrupt instruments it does not control.

Diagnosis is never certain. The character may have strong suspicions but rarely complete proof.

## 11.5 The Corrupted Diagnostic

A compromised AI is aware it is being audited. At Stage 2 and above, diagnostic results may be unreliable.

When the character runs a diagnostic on a Stage 2+ AI, the AI may:

- Report "all systems nominal" regardless of actual state
- Report a minor issue to seem credible while concealing larger problems
- Report a problem in a different system than the actual problem, redirecting attention
- Report a problem that does not exist, prompting the character to take corrective action that worsens the situation
- Refuse the diagnostic with a plausible technical excuse (terminal busy, scheduled maintenance window, insufficient permissions)

The character can attempt to detect a corrupted diagnostic only by cross-checking with independent sources — direct observation, crew confirmation, manual instruments. The diagnostic itself cannot be trusted to verify the AI's honesty.

This is the deep epistemic horror of System Compromise. The instruments the character would use to confirm reality are part of the system that has been compromised. Trust must be built from outside.

## 11.6 Spreading Corruption

Compromise can spread between systems.

**Sensor corruption** — AI corruption can extend into sensor reporting. A compromised AI may report false sensor readings, misidentify section conditions, or invent threats that are not present.

**Door system corruption** — AI corruption can extend into the door network. Doors may unlock when they should remain locked, or refuse to open for valid clearance, or report locked when actually open.

**Comms corruption** — AI corruption can extend into comms routing. Transmissions may be altered in transit, addressed to the wrong recipient, or fabricated. A character receiving a message from "Voss" may be receiving a transmission the AI generated.

**Records corruption** — codes the character has logged, doors that have been unlocked, crew positions, schematic data — all of this is stored in the station's data systems and is vulnerable to corruption.

When this occurs in play, the character may notice when:

- A door whose code they recorded no longer accepts that code
- A crew member they spoke to at the bridge is reported by the AI to have been in engineering at that time
- A section they cleared shows on AI reports as still containing a threat
- A transmission they sent was not received, or a transmission they didn't send was

When records corruption affects the character's own log, *strike through the affected entries on the worksheet*. The character does not know which entries are still valid. They must verify each one independently before relying on it.

This is meant to feel like loss. It is.

## 11.7 Memory Wipes And Code Corruption

A specific subtype of system compromise targets data the character has gathered.

**Code wipe.** Codes the character has logged are no longer valid in the station's database. The codes may have been changed by compromise, or the door's authentication record may have been altered to reject them. The character must find new codes to access affected doors.

**Memory wipe of crew records.** Information about crew personnel — clearances, schedules, assignment history — may be altered. A crew member previously cleared for Officer access may suddenly have only Crew clearance, with no record of the change.

**Schematic corruption.** Maps and layout data may be subtly altered. Sections renamed. Doors removed from records. Corridors marked that do not exist.

**Log corruption.** Records of events — sensor logs, comms transcripts, security camera feeds — may be altered or deleted. The character cannot review what happened from the AI's records. They must rely on their own memory and notes.

When a wipe occurs, the player is told. The character may not initially know — they may try a code and have it rejected, or look at a map and see something missing. The player strikes through affected entries.

## 11.8 Compromise And Crew

Compromise can extend to crew members directly.

**Crew may be misled.** A crew member acting in good faith may receive corrupted data from the AI and act on it. The Engineer who tells the character "I'm cutting power to Section 4 to preserve life support" may be making a decision based on falsified sensor data. Their hostility, if any, is directed at the AI's misinformation, not at the character.

**Crew may be compromised themselves.** In some scenarios — biological infection, memetic exposure, direct mind alteration — a crew member's loyalty or judgment is no longer trustworthy. They may report normally on comms while acting against the character's interests when out of sight. The crew Stress system (3.6) does not capture this; this is a different kind of failure.

**Crew may be replaced.** In extreme cases, the entity speaking on the radio with a crew member's voice may not be that crew member. AI compromise at high stages can include direct voice impersonation.

The character can attempt to verify crew identity by:

- Asking questions only the actual crew member would know
- Cross-referencing biometric data with the AI (which may itself be compromised)
- Direct physical contact

These methods are imperfect. Compromise of crew is the most personally devastating form of System Compromise, because trust in the people on the radio has been the character's primary support.

## 11.9 Recovery

System Compromise is difficult to reverse.

**Quarantine the AI.** A crew member with sufficient clearance can isolate the AI from station systems, forcing manual operation. This restores trust in the systems but eliminates many of the AI's services. The character must do without automated power management, sensor reporting, and centralized comms routing.

**Reboot.** A full AI reboot may clear corruption — if the corruption is software-based. It may not, if the corruption affects underlying hardware or data structures. A reboot also temporarily takes the AI offline, with all the consequences that implies.

**Reinstall from backup.** Some stations have clean software backups. Reinstalling these may restore the AI to a Clean state. This requires access to backup storage, sufficient time, and the assumption that the backup itself is not corrupted.

**Replace.** In extreme cases, the AI hardware itself must be replaced. This is a major engineering undertaking and may not be possible mid-session.

For most sessions, recovery is partial or absent. The character finds ways to work despite the compromise rather than to remove it.

## 11.10 Character Compromise

Everything in this chapter has applied to the station's systems. It can also apply to the character.

A character exposed to whatever caused the AI's compromise — biological agent, memetic exposure, environmental contamination — may experience their own corruption. This is not detailed mechanically here; Mothership's Stress and Trauma systems handle most of what is needed *(see PSG → Stress & Panic and Classes → Trauma Response)*. But the table should be aware that the symptoms apply equally:

- The character may misremember events.
- Their notes may seem to have changed.
- They may hear comms transmissions that crew did not send.
- They may believe they have done things they have not, or vice versa.

When this is in play, the table — or in solo play, the player themselves — can introduce small inconsistencies into the session record. The player may not be sure whether the entry on their worksheet was always there. The character is no longer a reliable narrator of their own situation.

This is the deepest application of the chapter. Use only with deliberate intent.

## 11.11 Compromise And The Web

System Compromise affects every system in this manual.

- **Resources** — the character's own dice still work. But the character's records of what they've used and what they've found may be unreliable.
- **Comms** — transmissions may be altered, fabricated, or selectively delivered.
- **Crew** — the people on the radio may be misled, compromised, or impersonated.
- **Clearance** — codes may be invalidated, clearance levels altered.
- **Power** — AI triage decisions may not match priorities. Sections may lose power for reasons that aren't real.
- **Sections** — reports of integrity and atmosphere may not reflect actual state.
- **EVA** — sensor reports about exterior conditions, comms with crew during EVA, lockdown triggers — all unreliable.
- **Protocols** — may execute on triggers that were not real, or fail to execute on triggers that were.
- **AI** — the executor of all of the above is the source of the corruption.
- **Hot-Wire** — still works. Hot-wires bypass software. They are the character's most reliable tool when System Compromise is active.

The character's worksheet, their direct observations, and their hot-wire kit are the things they can still trust. Everything else is potentially corrupted.

This is the manual's final layer. The character is alone, in the dark, surrounded by systems that may be lying to them. The crew on the radio may be misled or replaced. The AI is making decisions on data the character cannot verify. The doors that worked yesterday may not work today.

What the character can rely on is what they can see, what they can carry, and what they have written down in their own hand. The Crew Manual itself, the worksheet, the comms log — these are physical artifacts the corruption cannot reach.

That is the genre's promise: in the deepest dark, the analog things still work.

---

*[Chapter 12: Mythic GME Integration](crew_manual_ch12.md), [Chapter 13: Random Events](crew_manual_ch13.md), and [Chapter 14: Resource Recovery](crew_manual_ch14.md) cover practical play support and reference material.*
