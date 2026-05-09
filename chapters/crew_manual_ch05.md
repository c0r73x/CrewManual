# 5. POWER & SECTION STATUS

A station is not one place. It is many. Each section operates on its own power feed, its own life support, its own atmosphere. When one section loses power, the lights go out *there* — but not everywhere. The character can stand in a lit corridor and watch the door to the next section seal as that section's panel goes dark.

This chapter covers how power is tracked, how it fails, and how it spreads.

## 5.1 The Section Map

Before play begins, sketch the station as a map of connected sections. A section is any space that operates as a unit — a deck, a wing, a single large compartment. Granularity is up to the table, but most stations work well with five to twelve sections.

Each section needs:

- A name and a position on the map
- Which sections it connects to (doors and corridors)
- Initial Power state (default: Nominal)
- Initial Integrity state (default: Sealed)
- Initial Atmosphere state (default: Breathable)

Maintain the map throughout the session. Mark state changes in pencil so they can be updated. The map is a live document.

The character does not necessarily know the full map at session start. Discovery of layout is itself a scene. The crew may have access to schematics that the character can request via comms.

## 5.2 Power States

Each section tracks one of three power states.

**Nominal.** Lights on. Doors functional. Sensors active. Comms relays operating. Life support running normally. This is default operation.

**Brownout.** Lights flicker or run on emergency only. Doors cycle slowly. Sensors give intermittent readings. Comms have static. Life support runs at reduced capacity. The section is still survivable, but degraded.

**Dead.** No power. Lights are out — the character must use a Battery-powered lamp. Doors will not cycle remotely; they freeze in their current state. Sensors return nothing. Comms relays are dark; messages cannot pass through this section without alternate routing. Life support is off; atmosphere will degrade over hours unless restored.

A section's power state is independent of other states. A section in Brownout may still have full Atmosphere and Integrity. A Dead section may still be Sealed.

## 5.3 What Each State Affects

| Effect             | Nominal | Brownout              | Dead                     |
| ------------------ | ------- | --------------------- | ------------------------ |
| Lighting           | Full    | Emergency / flickering | Off (carry your own)     |
| Door operation     | Normal  | Slow, intermittent     | Frozen in current state  |
| Remote crew override | Yes  | Yes, with delay         | No                        |
| Comms relay        | Clear  | Static                  | Dead — message blocked   |
| Sensors            | Normal | Intermittent            | Offline                  |
| Life support       | Normal | Reduced                 | Off                       |
| Stress per scene   | 0      | +1                      | +1 on entry, +1 per scene |

Brownouts are recoverable through normal station operation. Dead sections require manual intervention — engineering work, hot-wires, or replacement of failed components.

## 5.4 Power State Changes

A section's power state can change from any of the following triggers:

- **AI Triage.** The Station AI may down-tier a section's power to preserve resources elsewhere (Chapter 8).
- **Cascade.** Power failure in one section may spread to adjacent sections (5.5).
- **Sabotage.** Deliberate action by the character, crew, or hostile force.
- **Damage.** Physical damage to power infrastructure from impact, fire, flooding.
- **Random Event.** Some Random Events specify power changes.
- **Restoration.** Engineering work, automated recovery, or hot-wiring.

State changes are not gradual within a single shift. A section either holds its current state or steps. Step changes happen at scene transitions or at the moment the triggering event resolves.

Always step in the direction of the change, by one tier:

- Nominal → Brownout
- Brownout → Dead
- Dead → Brownout (recovery)
- Brownout → Nominal (recovery)

A section cannot drop two tiers in a single change unless catastrophic (a hull breach into vacuum, for instance). A reactor failure may force multiple sections to drop simultaneously, but each by one tier.

## 5.5 Cascade

Power failures spread. When a section drops to Dead, roll 1d6 for each adjacent section. On a 1, that section drops one tier as well.

Cascade checks happen:

- Immediately when a section drops to Dead
- At the start of each subsequent scene, until the cascade is contained

Cascades stop when:

- An adjacent section is *isolated* from the affected one (manually disconnecting power cabling — engineering work, often crew action)
- The originating fault is repaired
- The cascade reaches the limits of the affected power grid

A cascade is the system's way of expressing infrastructure as living, contagious failure. Once one section goes dark, the rest is a clock.

> *EXAMPLE.* Section 3 drops to Dead due to AI triage. The character watches the lights cut. Adjacent sections are 2, 4, and 7. Roll 1d6 for each: Section 2 rolls a 1. Section 2 drops Nominal → Brownout. Sections 4 and 7 hold. Next scene, roll again. Section 2 rolls a 4 (holds), but Section 4 rolls a 1 — it drops to Brownout. The dark is spreading.

## 5.6 Restoring Power

Power can be restored to a Brownout or Dead section through several routes.

**Engineering work.** A crew member with Engineering skill, at a working engineering panel, can attempt restoration. Success requires:

1. Comms contact with the engineer (1 Battery Charge)
2. Engineer at a functional engineering station (not in a Dead section themselves)
3. Successful Engineering roll
4. Time — typically 1 to 3 scenes for full restoration

**Automatic recovery.** If the cause of failure is removed (AI triage lifted, fire suppressed, breach sealed), some sections recover automatically over time. Roll 1d6 each scene; on a 5 or 6, the section steps up one tier.

**Hot-wire bypass.** The character can hot-wire a single device (a door, a terminal, a lamp) to function temporarily without restoring section power. See Chapter 10.

**Reserve power activation.** Stations have emergency reserves. A crew member with Officer or Executive clearance, at the bridge or at a reactor control, can activate reserves. This restores Brownout sections to Nominal for a limited duration (typically one shift). Reserves themselves are a finite resource.

Restoration is never instant. The character may need to push through several scenes in a Dead section before help arrives.

## 5.7 Stress And Degraded Power

Power loss is not just inconvenient. It is psychologically wearing.

- Entering a Brownout section: no automatic Stress, but +1 per scene of continued operation in the section.
- Entering a Dead section: +1 Stress immediately, +1 per scene.
- The character can adapt — long exposure to one degraded section reduces the per-scene increase to 0 after three scenes. The fear becomes background.
- A *new* degradation (a section the character was in dropping to Dead while they were still inside) always triggers a fresh Stress gain.

Use these triggers in addition to Mothership's standard Stress events. Power degradation is environmental horror; it stacks with whatever else is happening.

## 5.8 Power And The Web

Power state is the underlayer of nearly every other system in this manual.

- **Comms** require working power on both ends *and* in any relay sections between.
- **Doors** require power in the door's section to open or close on command.
- **Crew functions** require their station to have power.
- **Sensors and AI reporting** require power throughout the affected sensor array.
- **Life support** failure is itself a power problem (5.3).

When the character cannot make something work, ask first: *Is there power here?* It is the most common silent cause of failure. The character may be calling a crew member who is alive, willing, and able — but in a section that has just dropped to Dead, and they cannot answer.

The dark is rarely just dark. It is the absence of every other system at once.

---

*Chapter 6 — Section Integrity & Atmosphere — covers the other two state tracks each section maintains, including hull breaches, flooding, and the kinds of environments that kill without power even being relevant.*
