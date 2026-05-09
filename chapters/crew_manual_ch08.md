# 8. STATION PROTOCOLS & LOCKDOWN

A station is not just a structure. It is a structure governed by automated rules. These rules — protocols — execute without human intervention when their triggering conditions are met. They are designed to preserve life, contain damage, and protect assets in priority order, in that exact priority order, regardless of who is currently in the way.

This chapter covers the protocols that run the station, including the lockdown procedures referenced earlier in this manual.

## 8.1 What Protocols Are

A protocol is a stored set of automated responses keyed to a sensor reading or condition. When the trigger fires, the protocol executes. Crew may be notified, but the protocol does not wait for permission.

Protocols are designed by the station's operator — typically a corporate entity with priorities that may not match the crew's. A research station's quarantine protocol may prioritize containing data over preserving crew. A mining station's reactor protocol may prioritize hull integrity over crew in the affected sections.

The character cannot turn off protocols casually. Protocols are baked into station systems. They can be overridden — temporarily, with appropriate clearance — but the override itself must be authorized and is often logged.

The Station AI (Chapter 9) is the primary executor of protocols. When the AI is functioning normally, protocols run as designed. When the AI is compromised (Chapter 11), protocols may run incorrectly, partially, or not at all.

## 8.2 Common Protocol Types

Most stations carry some version of the following:

| Protocol             | Triggered By                                   |
| -------------------- | ---------------------------------------------- |
| Lockdown             | Detected exterior threat, hull breach, intrusion |
| Quarantine           | Biohazard, contamination, unidentified organism |
| Evacuation           | Catastrophic damage, reactor critical, atmospheric loss |
| Reactor Scram        | Reactor instability, cooling failure, overpressure |
| Fire Suppression     | Detected fire or smoke                         |
| Atmospheric Purge    | Toxic atmosphere alert in sealed section       |
| Communications Black | Hostile signal interception, classified operation |
| Power Triage         | Insufficient power for full station operation  |

Specific stations may have proprietary protocols. A research station may have a "Sample Containment" protocol. A military installation may have "Defense Posture." These are flavored versions of the standard list.

When setting up a session, the table should establish which protocols are active and what their triggers are. The character may not know all of them — discovering an unexpected protocol in execution is itself a horror scene.

## 8.3 Lockdown

Lockdown is the protocol most likely to affect the character directly.

**Triggers:**

- Hull breach detected
- Exterior threat (large biological, hostile vessel, environmental hazard)
- Intrusion (unauthorized boarding, internal forced entry)
- Manual activation by Officer-or-higher clearance
- Cascading section failures suggesting catastrophic loss

**Effects:**

- All EVA airlocks lock to exterior. Cannot cycle outward without override. Inward cycling may be restricted depending on lockdown severity.
- Section bulkheads close and seal. Sections become independent compartments.
- Inter-section comms may be restricted to emergency channels.
- Power may be redirected to defensive priorities (sensors, communications, security systems) at the expense of normal operations.
- Crew movements between sections are restricted.

**Severity Levels:**

| Level   | Description                                              |
| ------- | -------------------------------------------------------- |
| Soft    | Bulkheads sealed; airlocks locked; comms unrestricted    |
| Hard    | All of Soft, plus comms restricted to emergency frequency |
| Total   | All of Hard, plus override-resistant; only Executive can lift |

A Soft lockdown is recoverable through normal command channels. A Total lockdown means the station has determined the threat is severe enough to override standard operating procedure entirely.

**Lifting Lockdown:**

- **Trigger resolution.** The condition that caused lockdown is no longer present. Hull patched, threat departed, intrusion neutralized. Some triggers auto-clear; others require manual confirmation.
- **Manual override.** Crew with appropriate clearance can lift lockdown from a command terminal. Officer clearance for Soft, Officer or Executive for Hard, Executive only for Total.
- **Section-specific override.** Some lockdowns can be lifted in one section while remaining active elsewhere. A captain may unlock the bridge airlocks while keeping the rest of the station sealed.

A character outside during lockdown faces the situation described in 7.11. A character inside during lockdown is sealed in their current section until the protocol lifts or is overridden.

## 8.4 Quarantine

Quarantine protocols isolate sections suspected of biohazard.

**Triggers:**

- Contamination sensor activation
- Unknown biological signature detected
- Reported infection by crew
- Manual activation

**Effects:**

- Affected section sealed; doors will not cycle outward to non-quarantine areas.
- Atmospheric circulation cut between quarantine zone and rest of station.
- Crew in quarantine zone cannot leave without override.
- Material transfer in or out is blocked.

Quarantine is often more durable than Lockdown. It is intended to last hours to days, not minutes. Lifting quarantine requires confirmed all-clear scans, which may not be possible without specialist equipment.

A character trapped in quarantine has limited options:

- Find an authorized override (crew, code, or Executive clearance)
- Hot-wire the door (Chapter 10) — with the understanding that doing so may release whatever the quarantine was meant to contain
- Find an alternate route that bypasses the seal
- Wait for the quarantine to lift on a confirmed all-clear

Hot-wiring quarantine is a difficult moral and tactical choice. The protocol exists to protect the rest of the station. Defeating it may save the character at others' expense.

## 8.5 Evacuation

Evacuation protocols are triggered when the station has determined that further occupation is untenable.

**Triggers:**

- Reactor failure imminent (typically defined as time-to-criticality below threshold)
- Catastrophic structural failure
- Atmospheric loss across multiple sections
- Manual activation by Captain or Executive clearance

**Effects:**

- Lifeboat / escape pod systems unlock and prepare for launch
- Audible alarms throughout station
- Power priority shifts to evacuation routes (corridors to lifepods, airlocks to lifeboats)
- Non-essential systems may be powered down to extend evacuation window

An evacuation protocol is generally to the character's benefit — the station is telling them to leave, and providing the means. But evacuation does not wait. If the character is doing something they consider more important than leaving, the lifeboats will eventually launch with or without them. Some protocols include automated launch on a timer, in which case missing the window means missing the only ride.

Evacuation also conflicts with other protocols. If lockdown and evacuation are simultaneously active, the priority depends on the station's design — usually evacuation takes precedence, but not always.

## 8.6 Reactor Protocols

Reactor scram and related protocols handle power generation emergencies.

**Triggers:**

- Reactor instability or imminent meltdown
- Cooling system failure
- Overpressure or radiation leak
- Manual scram by appropriate clearance

**Effects:**

- Reactor shuts down, often with a controlled or emergency procedure
- Station shifts to reserve power
- AI Power Triage activates (Chapter 9): non-essential systems lose power
- Some sections drop to Brownout or Dead immediately
- Engineering personnel may be locked into the reactor section to perform manual procedures

A reactor protocol is an instant station-wide event. The character will feel it as a sudden change in the lighting, sound, and atmosphere. Things that were working a moment ago no longer are.

Recovering from a reactor scram is an extended process — often a session-long effort to restart, repair, or supplement power generation.

## 8.7 Other Protocols

Brief notes on protocols not detailed above:

- **Fire Suppression.** Triggers on smoke or heat detection. Vents atmosphere from affected section, deploys foam or other suppressants. May damage equipment in suppressed area. The character caught in a fire suppression activation may face atmospheric loss in addition to whatever caused the fire.
- **Atmospheric Purge.** Vents toxic atmosphere from a section. Temporarily creates Vacuum or near-Vacuum in the affected space, requiring suit operation. Followed by atmospheric refill if life support is functional.
- **Communications Black.** Signals an external transmission halt. Outgoing comms may be restricted to authorized signals only. Used during corporate-sensitive operations or hostile presence.

Each protocol can be combined with others. A station experiencing reactor scram, lockdown, and evacuation simultaneously is a station whose systems are competing for priority — and the AI is making decisions about who lives and who waits.

## 8.8 Manual Override

Most protocols can be overridden by crew with appropriate clearance, working at a working terminal in a powered section.

**Procedure:**

1. Crew member must be at a command-capable terminal. Not all terminals can issue overrides; bridge stations, security centers, and specifically authorized engineering panels typically can.
2. Crew member must have clearance equal to or higher than the protocol's authorization level.
3. Comms must be available between the character and crew (or the crew is acting on their own initiative).
4. Roll the crew member's relevant skill — usually Computers — at -10 to -30 depending on the protocol and station condition.
5. On success, the protocol is overridden for a stated duration or until restated. On failure, the override is rejected; the system may log the attempt.

**Cost:**

Overriding a protocol is not free. Most stations log overrides. Some require Executive sign-off after the fact. Some trigger secondary alerts to corporate or external authorities. The character who relies on overrides may find the consequences arrive later, off-station.

## 8.9 Conflicting Protocols

When two or more protocols trigger simultaneously, they may conflict. Each protocol has a priority value baked into its programming. The AI executes higher-priority protocols first, then resolves lower-priority ones to the extent compatible.

Default priority order (most to least):

1. Reactor Scram
2. Evacuation
3. Lockdown (Total)
4. Quarantine
5. Lockdown (Hard / Soft)
6. Fire Suppression
7. Atmospheric Purge
8. Power Triage
9. Communications Black

A station whose operator has different priorities may reorder this list. A research facility may put Quarantine above Evacuation. A military installation may put Communications Black very high.

When protocols conflict, the character may experience contradictory signals: lockdown engages while evacuation alarms sound; the AI directs them toward an airlock that lockdown has just sealed. This is the system fighting itself, and it is genuinely dangerous.

## 8.10 Setting Up Protocols

At session start, the table establishes:

- Which protocols are present on this station
- What conditions trigger each
- The priority order
- Any custom or proprietary protocols

For solo play with the oracle, default to the standard list above. Add custom protocols when the scenario calls for them — a research station with a Sample Containment protocol, a military installation with a Defense Posture protocol.

The character's knowledge of station protocols is not always complete. They may know the basics — lockdown exists, quarantine exists — but not the specific triggers, priorities, or override authorities for *this* station. Discovering these mid-session, often by being affected by them, is part of play.

A protocol acting unexpectedly is not necessarily a corruption symptom. Sometimes the protocol is doing exactly what it was designed to do, and the character did not know what that was.

---

*Chapter 9 — Station AI — covers the system that executes these protocols, prioritizes power and resources, and may not always be doing what its operators believe it is doing.*
