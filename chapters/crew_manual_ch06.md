# 6. SECTION INTEGRITY & ATMOSPHERE

Power is one third of what each section tracks. The other two are Integrity (the structural and environmental seal of the section) and Atmosphere (what the character will breathe if they remove their helmet). These three states are independent — a section can have full Power, no Atmosphere, and a hairline breach in Integrity, all at once.

This chapter covers the second and third state tracks, multi-structure station layouts, and what happens when the inside of the station starts becoming the outside.

## 6.1 Integrity And Atmosphere

Integrity is whether the section is *sealed* — whether its hull, walls, doors, and seals are keeping the inside in and the outside out.

Atmosphere is what fills the section's interior space. Air. Vacuum. Water. Toxic gas. A combination.

The two interact but are distinct. A Compromised section may still have breathable atmosphere (a small leak that life support is keeping up with). A Sealed section may have lost atmosphere (life support failure with intact walls). These distinctions matter for what equipment the character needs to enter, and what risks they take.

## 6.2 Integrity States

| State        | Description                                  |
| ------------ | -------------------------------------------- |
| Sealed       | Walls intact. Doors holding pressure. No leakage. |
| Compromised  | Hairline breach, slow leak, partial seal failure. Life support may compensate temporarily. |
| Vacuum       | Section open to vacuum or near-vacuum. Total integrity loss to space, or controlled depressurization. |
| Flooded      | Section open to water or fluid pressure from outside. Filled or filling. |

Sealed is the default. Stations are built to hold pressure. When integrity degrades, it usually does so because of damage, sabotage, or design failure — not as part of normal operation.

A Compromised section is a clock. The compromise is either widening (further degradation in scenes ahead) or stable (life support compensates indefinitely). The oracle decides which when relevant.

Vacuum and Flooded are catastrophic states. They typically require EVA equipment to enter and survive. See Chapter 7.

## 6.3 Atmosphere States

| State          | Description                                  |
| -------------- | -------------------------------------------- |
| Breathable     | Standard atmosphere. Character can operate without sealed equipment. |
| Toxic / Thin   | Atmosphere present but harmful or insufficient. Mask or filter required. |
| Vacuum         | No atmosphere. Sealed suit required. |
| Flooded        | Filled with water or fluid. Diving equipment required. |

Toxic and Thin are grouped because they share a mechanical response: the character needs filtered breathing equipment. The fictional difference is significant — toxic atmosphere may corrode equipment, thin atmosphere may merely require supplemental O2 — but the procedural answer is the same: do not breathe this without a filter.

Atmosphere can shift independently of Integrity. A life support failure can void a Sealed section. A breach can pull breathable atmosphere into vacuum within minutes.

## 6.4 Stations As Multiple Structures

Throughout this manual, "station" has been used as if it meant a single connected interior. This is the simplest case, but not the only one.

A station may be:

- **A single complex.** All sections connected by interior corridors and doors. Standard space station, large vessel, sealed habitat.
- **Multiple structures connected by enclosed transit.** Tubes, walkways, pressurized passages between separate buildings. Common on planetary surfaces and undersea.
- **Multiple structures requiring environmental transit.** Buildings on a hostile planet's surface, or on the ocean floor, where moving between them requires EVA-equivalent gear and traversing the outside environment.
- **Mixed configurations.** A central complex with outlying stations connected by various means, some sealed, some exposed.

When designing the section map, indicate which connections are *interior* (cross with a normal door) and which are *transit* (cross by EVA, by submersible, by walking across the surface in a sealed suit).

In a multi-structure station, each structure has its own:

- Power grid (cascades stop at the structure boundary)
- Section map (interior layout)
- Comms relays (signals between structures may be limited or relayed)
- Life support (atmosphere is local to each structure)

This is the SOMA configuration. The PATHOS-II layout. Multiple isolated facilities on the seabed, each its own ecosystem of failure, connected by lifeline cables and the long dark between.

> *EXAMPLE.* A research outpost consists of three structures: Main Hab, Power Annex, and Sample Lab. Main Hab and Power Annex are connected by an enclosed pressurized walkway. Sample Lab is two hundred meters away across the planet's surface — reaching it requires donning a suit and walking. The character can move freely between Main Hab and Power Annex through the walkway. Reaching Sample Lab is a full EVA scene with O2, atmosphere checks, and exposure to whatever is out there.

The crew may be distributed across structures. The Captain on Main Hab. The Engineer at Power Annex. The Scientist isolated in Sample Lab. When inter-structure comms are interrupted — by distance, by relay failure, by hostile interference — crew members in different structures cannot reach each other. The character may become the only thing that can carry messages.

## 6.5 State Change Triggers

Integrity and Atmosphere can change due to:

- **Damage.** Impact, fire, explosion, structural failure.
- **Sabotage.** By the character, the crew, or hostile force.
- **Cascade.** Failure in one section affecting adjacent sections (6.6).
- **Life support failure.** Atmosphere degrades when its supporting system fails.
- **Random Event.** Some Random Events specify state changes.
- **Environmental hazard.** A section already Compromised may worsen due to outside pressure, temperature, or chemistry.

State changes for Integrity and Atmosphere are usually one tier at a time:

- Sealed → Compromised → Vacuum *or* Flooded
- Breathable → Toxic/Thin → Vacuum *or* Flooded

Catastrophic events (explosive decompression, hull rupture into ocean) can skip tiers, dropping a section from Sealed directly to Vacuum or Flooded. Use this for major dramatic moments, not casual changes.

## 6.6 Cascade

Integrity and Atmosphere cascade similarly to Power, but the rules differ slightly.

When a section drops to **Vacuum** or **Flooded**, roll 1d6 for each *interior-connected* adjacent section:

- On a 1: that section drops one tier in Integrity (Sealed → Compromised) and possibly Atmosphere if relevant (Breathable → Toxic, if a Toxic adjacent atmosphere is present, or Breathable → Vacuum if connected to Vacuum).
- On 2 or higher: the connecting door or seal holds. The cascade is contained at that boundary.

Cascade does not cross transit connections in multi-structure stations. A Flooded structure's neighbor — connected only by external transit — does not catch a flood. But its connecting tube may. If the tube is its own section (and it should be, in such layouts), the tube itself may flood, isolating the structures further.

A cascade in Integrity and Atmosphere is faster and more dangerous than Power cascade. It can kill in scenes, not shifts. Containment is critical.

## 6.7 Detection

The character does not always know a section's true state until they are in it — or near it.

When approaching a section, the character may:

- **Check sensors** if they have a working terminal in a section with sensors and Power. Sensors in Brownout are intermittent; in Dead, offline.
- **Ask crew** if a crew member has access to monitoring stations and is in comms.
- **Observe directly** — pressure differential at doors, frost, condensation, water on the floor of the corridor.
- **Look through the window** if there is one. Many doors have viewports.

If the character has none of these and must enter blind, the oracle determines what they find. *Is the section as expected?* Mythic Likelihood depends on what the character last knew about it.

False sensor readings are possible, especially if AI systems are compromised (Chapter 11). The Captain may report "Section 4 nominal" when in fact Section 4 has been Compromised for an hour. The character cannot always trust what they are told.

## 6.8 Restoration

Restoring Integrity and Atmosphere is more difficult than restoring Power.

**Atmosphere** can be restored by life support if the section is Sealed and Power is at least Brownout. Time depends on section size — typically 1 to 3 scenes for breathable atmosphere to return. Toxic atmosphere requires venting first, then re-supply.

**Integrity** can be restored by:

- **Manual repair.** Patching a breach with sealing foam, welding plates, jamming damage with available materials. Engineering skill. May only restore Compromised → Sealed; fully Vacuum or Flooded sections often require a controlled re-pressurization that takes shifts, not scenes.
- **Section isolation.** Sealing the section off from the rest of the station so it cannot threaten others. Does not restore the section, but stops its cascade.
- **Crew engineering work.** A skilled engineer with materials and a working access point can attempt full restoration. This is a multi-scene project.

Restoration to a Vacuum or Flooded section is exceptional and almost always involves at least one EVA scene (Chapter 7) to access the affected zone from outside.

## 6.9 The Compromised Section In Play

Most of this chapter has covered binary or near-binary states. But the Compromised state — and Toxic atmosphere — are *durations*, not events. They are conditions the character must live with, sometimes for entire sessions.

A Compromised section is survivable. Suit pressure can compensate. Life support may keep atmosphere breathable. But:

- The Compromised state ticks toward Vacuum or Flooded. Each scene the character spends in a Compromised section, roll 1d10. On a 1, the compromise widens — the section drops to Vacuum or Flooded.
- Repairs do not last unless properly done. A patch with sealing foam is temporary.
- Stress accrues. +1 per scene in a Compromised section that the character cannot leave.

A Compromised section is a place where the character is racing the building itself. They must do what they came for and leave before the seal fails.

## 6.10 Stress And Other Effects

Stress modifiers from Integrity and Atmosphere stack on top of Power-state modifiers and any Mothership-standard Stress events.

| Section State                | Stress per Scene |
| ---------------------------- | ---------------- |
| Sealed, Breathable, Nominal Power | 0           |
| Compromised Integrity         | +1              |
| Toxic / Thin Atmosphere       | +1              |
| Vacuum or Flooded             | +1 entry, +1 per scene |
| Multiple states degraded      | Stack effects    |

A Compromised, Brownout, Toxic section is a horror scenario. Stress accrues quickly; the section punishes lingering.

Use these modifiers in combination with the section map to design or run sessions where geography matters. A character knows they need to reach Section 7. They know Sections 5 and 6 are in poor state. The route itself is a series of decisions: which way through? Which sections can they survive? How long can they stay?

The station, in this configuration, is an antagonist made of geometry and decay.

---

*[Chapter 7: EVA & Submersion Operations](crew_manual_ch07.md) covers what the character does when they have to leave the safe interior, traverse the outside, or enter a section that no longer welcomes anything alive.*
