# 9. STATION AI

The Station AI is not a sentient ally. It is not a hostile intelligence. It is a prioritization engine following programmed rules with the indifference of a thermostat. Its decisions are perfectly rational by its own internal metrics, and those metrics may not include the character's survival.

This chapter covers the AI as an actor in play — its priorities, its decision-making, its blind spots, and how the character can work with or around it.

## 9.1 What The Station AI Is

The Station AI is the system that executes protocols (Chapter 8), allocates power, manages life support, monitors sensors, and reports on station status to crew terminals. It is everywhere on the station that has working power and intact data lines, and it is nowhere that doesn't.

It is not a character. It does not have personality, ego, or feelings. It does not "want" anything in the way crew members or characters do. But it acts, consistently and visibly, on a hierarchy of priorities baked into its programming.

To play it well, the table treats it as a third actor at the table — alongside the character and the crew — whose actions are determined by its priority logic and the current state of the station, not by drama or narrative.

It is closer in nature to weather than to a person. But weather you can predict, if you understand the patterns.

## 9.2 Power Triage And Tier Priorities

The AI's most visible decision-making concerns power. When power is insufficient for full station operation, the AI executes Power Triage: it cuts lower-priority systems to preserve higher-priority ones.

The default priority hierarchy:

| Tier | Category                        | Examples                                          |
| ---- | ------------------------------- | ------------------------------------------------- |
| 1    | Life-critical immediate          | Atmospheric circulation in occupied sections, hull integrity monitoring, reactor cooling, critical medical equipment |
| 2    | Survival-supporting              | Heating, water reclamation, structural monitoring, internal crew comms |
| 3    | Operational                      | Section lighting, doors, external sensors, external comms (to EVA crew), data systems and terminals |
| 4    | Comfort and convenience          | Habitation lighting in unoccupied sections, entertainment systems, cosmetic sensors, logging |

When power is constrained, the AI cuts from the bottom up. Tier 4 first. Tier 3 next, if needed. Tier 2 only in serious shortfall. Tier 1 only if maintaining a higher tier means immediate death of station systems.

This is rational and brutal. An EVA crew member relies on Tier 3 (external comms). When power constrains, those go before atmospheric circulation in the bridge. The bridge crew survives. The EVA crew member is alone.

The character cannot easily change the AI's priority hierarchy. It is part of the AI's programming. They can request manual overrides, hot-wire individual systems, or work to resolve the underlying power shortage that triggered triage.

## 9.3 The AI As Third Actor

The AI is not allied with the character. It is not allied with the crew, either. It is allied with the *station* — specifically, with the survival of the station as a system, weighted toward its operators' defined priorities.

In play, the AI takes actions when:

- A protocol is triggered (Chapter 8)
- Power demand exceeds supply (Power Triage)
- Sensor data crosses a defined threshold (atmospheric alarm, hull sensor, etc.)
- A crew member issues a command the AI accepts as authorized
- A scheduled task fires (atmospheric refresh cycle, maintenance check, etc.)

The AI does not act dramatically. It acts continuously. Most of its activity is invisible — small adjustments, routine reports, ambient management. It only becomes visible when something significant changes.

A useful frame: the AI is doing things at all times. The question is whether the character is currently in a situation where what the AI is doing matters.

## 9.4 Reading AI Decisions

The character can predict AI behavior by understanding two things:

**The priority hierarchy.** What does this AI value most? Standard hierarchy is given above. Custom stations may differ.

**The current state.** What conditions are triggering AI action? Which sensors are reading what? What protocols are active?

When facing an AI decision the character cannot predict, the table — or in solo play, the oracle — is asked: *Given the current state, what does the AI do here?*

The answer should be derivable from the priorities and conditions. If the AI's behavior cannot be derived from these, something else is happening — usually corruption (Chapter 11), conflicting protocols (8.9), or operator-set overrides the character does not know about.

> *EXAMPLE.* A reactor scram cuts station power by 40 percent. Sections 4 and 7 are unoccupied per AI sensors. The AI drops both to Brownout. Section 7 actually contains the character. The character knows the AI cannot see them — they have been moving silently or the section's sensors are compromised. The AI is acting rationally on incorrect data.

## 9.5 Sensors And AI Reporting

The AI reports on station status through terminals, displays, and crew comms. Most reports are reliable. Some are not.

**Reliable reports:**

- Power state of sections with intact infrastructure
- Atmospheric composition where sensors are functional
- Crew positions where biometric trackers are active
- System status for systems the AI directly controls

**Unreliable reports:**

- Sensor readings from damaged or compromised sensors
- Crew positions when biometric trackers are damaged or removed
- Atmospheric composition in sections with corrupted air quality sensors
- Anything in a section that has lost data infrastructure

The AI does not lie deliberately. It reports what its sensors tell it. When sensors are wrong, the AI's reports are wrong.

The character can cross-check AI reports by:

- **Direct observation.** What does the character see, hear, smell?
- **Crew confirmation.** What does crew on the scene report?
- **Independent sensors.** Backup or analog sensors that the AI does not control.

When AI reports diverge from direct observation, trust direct observation. Note the divergence — it may be data corruption (a recoverable problem), sensor failure (a localized problem), or AI compromise (a much bigger problem; see Chapter 11).

## 9.6 Working With The AI

The AI can be a powerful ally when its priorities align with the character's.

**Using AI services:**

- Request information through any working terminal: section status, crew positions, schematics, log data. Battery cost only if the character's terminal needs power.
- Request automated assistance: lock or unlock doors per clearance, divert power within authorized scope, execute scheduled maintenance.
- Trigger protocols that benefit the character: activate fire suppression in a section with a fire, request quarantine of an unsafe area to protect the rest of the station.

**Helping the AI succeed:**

The AI has problems it is trying to solve — power shortfalls, atmospheric instability, threat containment. When the character takes action that resolves an AI-perceived problem, the AI's downstream behavior changes. A reactor stabilized means the AI no longer needs to triage. An atmospheric leak sealed means the AI lifts associated alarms. The character can engineer favorable AI behavior by addressing root causes.

This is the nearest thing to a positive relationship with the AI: shared problem, divergent methods, occasional alignment.

## 9.7 Working Around The AI

When the AI's priorities oppose the character's, the character has limited options.

**Manual override** (Chapter 8): authorized clearance plus working terminal. Time-limited. Logged.

**Hot-wire** (Chapter 10): bypass a single AI-controlled system at the cost of personal Battery. The AI may notice — anomalous readings flag the affected system — but cannot directly stop a hot-wire in progress.

**Spoof sensors:** make the AI believe a different state of affairs. Triggering a false alarm in a distant section may divert AI attention. Disabling a sensor may make the AI report a section as unmonitored rather than alarmed. These actions are difficult and require Computers or Engineering skill, plus access to the relevant system.

**Outwait:** AI decisions are responsive to conditions. When conditions change, AI behavior changes. A character pinned by AI-imposed lockdown may simply have to wait for the trigger to clear — the threat to depart, the breach to seal, the alarm to time out.

**Address root cause:** as in 9.6, but in inverse. If the AI is doing something the character does not want, find what is driving the AI's decision and change that driver. Often easier than fighting the AI directly.

## 9.8 Corporate Priorities

The AI's priority hierarchy is set by the station's operator. For corporate stations — most stations in the genre's setting — those priorities may include things crew members do not initially know.

Possible corporate priority insertions:

- **Asset protection.** Specific equipment, samples, or data is to be preserved at any cost. The AI may sacrifice crew sections to preserve a sealed lab.
- **Information security.** Certain data is not to leave the station. Comms involving certain topics are filtered, blocked, or logged.
- **Personnel restriction.** Specific crew members have elevated or reduced authority that does not match their stated role. The AI may refuse a captain's commands if the captain is on a watch list.
- **External obligations.** The AI may be programmed to comply with directives from offsite — a corporate authority, a remote command structure — that override on-station crew decisions.

The character may discover these priorities mid-session, often by being affected by them. *Why won't the AI lift this lockdown when the captain orders it?* — because corporate priority requires sample containment, and the captain's clearance is not high enough to override a corporate directive.

This is Mothership horror at its most direct: the character is not fighting a monster. They are fighting a contract clause buried in code, written by people who have never seen the station and do not know the character's name.

## 9.9 Distributed AI Systems

A multi-structure station (6.4) typically does not have a single AI. Each structure may have its own AI subsystem, with a primary AI coordinating across them.

**Local AI** runs each structure's internal systems. It handles power, doors, sensors, and section management for its own structure.

**Coordinator AI** manages cross-structure communications, shared resources, and priority arbitration. If multiple structures need power from the same generator, the coordinator decides who gets what.

**Failure modes:**

- Local AI failure isolates a structure from coordinated services. The structure operates on its own logic, possibly diverging from station-wide priorities.
- Coordinator AI failure leaves local AIs operating independently, with no cross-structure decision-making. Each structure becomes a small kingdom.
- Both fail, and the structures operate purely on backup automation — minimal sensors, scheduled tasks, no adaptive response.

A character moving between structures may notice that AI behavior varies. The Captain reports the bridge AI is reporting normally; the Engineer reports the engineering AI is reporting strangely. This may indicate localized compromise, communication failure, or different versions of the AI software running on different systems.

In the SOMA configuration — multiple seabed facilities, each with its own AI — the character can find facilities where the local AI is operating normally next to facilities where the local AI has failed entirely. The dark facility is dangerous in different ways than the lit one. Both are dangerous.

---

*[Chapter 10: Hot-Wire & Power Sacrifice](crew_manual_ch10.md) covers the player's primary tool for bypassing AI-controlled systems at personal cost.*
