# 4. SECURITY CLEARANCE

Most doors aboard a station are not just doors. They are checkpoints. The character's ability to pass through them is gated by clearance level, working power, intact data systems, and sometimes a code the character does not have.

This chapter covers how access works, how it fails, and how the character can sometimes get through anyway.

## 4.1 Clearance Levels

A standard station uses three primary clearance levels, plus a parallel maintenance track.

| Level       | Color  | Access                                        |
| ----------- | ------ | --------------------------------------------- |
| Crew        | White  | Corridors, mess, common areas, basic stations |
| Officer     | Yellow | Bridge, infirmary, weapons, navigation, comms |
| Executive   | Red    | Labs, classified storage, captain's quarters  |
| Maintenance | Grey   | Vents, conduits, service tunnels, utility crawlspaces |

Clearance is hierarchical for the primary track: Executive can access Officer and Crew areas. Officer can access Crew areas. Crew is baseline.

Maintenance runs parallel. A Crew-clearance maintenance worker can access service spaces an Executive cannot, because the Executive was never issued maintenance credentials. This is intentional in station design: critical infrastructure is reachable by the people who actually need to fix it, not necessarily by the people who command them.

## 4.2 Door Types

Every locked door has a type. The type determines what unlocks it.

**Open.** Not locked. Not tracked. Just doors.

**Clearance-Locked.** Requires a credential of sufficient level. The character's own clearance opens it, or a crew member with appropriate clearance can issue a remote override (4.4).

**Code-Locked.** Requires a specific numeric or alphanumeric code. Codes must be found — overheard, written down, recovered from terminals, transmitted by crew. Codes are not guessable.

**Biometric-Locked.** Requires a specific person's biometric signature. If that person is dead, the lock can sometimes be defeated by physical means: cutting open the panel, hot-wiring (Chapter 10), recovering and using the body. Biometric overrides are slow and noisy.

**Mechanical.** No electronics. Manual valves, sealed bulkheads, blast doors with hand cranks. Power state does not matter. They are opened by physical effort and time.

A single doorway may combine types. A blast door requiring Executive clearance *and* a code is not unusual in classified sections.

## 4.3 The Door Procedure

When the character encounters a locked door:

1. **Identify the door type.** Read the panel, observe the locking mechanism. If unclear, ask the oracle.
2. **Check the character's own access.** Does the character's clearance match? Do they have the code?
3. **If not accessible directly, choose:**
   - **Call crew for remote override** (4.4)
   - **Find another way** (alternate route, often longer, often through hostile sections)
   - **Hot-wire the door** (Chapter 10)
   - **Force the door** (mechanical only — slow, loud)
4. **Resolve the chosen approach.**

The character may always retreat and try a different approach later. A locked door is not a wall. It is a question of cost.

## 4.4 Calling Crew For Override

A crew member with appropriate clearance, at a working terminal, with comms intact, can remotely unlock most clearance-locked doors.

To request a remote override:

1. **Establish comms** with the crew member. Use the Comms Procedure (3.4). Costs 1 Battery Charge.
2. **Verify their access.** The crew member must have clearance equal to or higher than the door requires. Officer clearance opens Officer doors. Executive opens all clearance-locked doors.
3. **Verify their station.** The crew member must be at a working terminal in a section with power. A captain on the bridge can issue overrides; a captain in a corridor cannot.
4. **Verify door system.** The door must be in a section with power and uncompromised data systems. A door in a Dead section cannot be remotely overridden.
5. **Roll the crew member's relevant skill** if the override is non-routine — for example, overriding a flagged security door, or working around a system anomaly. Computers or Engineering as appropriate.
   *(See PSG → Stats & Skills for skill check resolution.)*
6. **Resolve.** On success, the door cycles open. There is a delay — typically one round, sometimes longer.

> *EXAMPLE.* The character is at a Yellow-clearance door in Section 3. They call the bridge. The Captain is on station. Section 3 has nominal power. The bridge has nominal power. Comms is clear. The Captain issues the override. The door cycles open. Total cost: 1 Battery Charge.

> *EXAMPLE.* The same door, but a power brownout has hit Section 3 since the character last checked. The override goes through on the bridge's end — the Captain confirms the command was sent — but the door does not open. The character now knows the section is in trouble.

## 4.5 Codes

Codes are physical game material. When the character finds a code, write it down. When the character uses a code, mark the door it opens. When a code is lost — wiped, expired, revoked — strike it through.

Codes are recovered from:

- **Terminals.** Decryption rolls (Computers). Successful roll yields one code. Time-consuming and battery-expensive.
- **Logs and notes.** Personal logs on tablets, sticky notes under keyboards, handwritten ciphers in notebooks. Often found on or near bodies.
- **Crew transmission.** A crew member with access to records can read out a code. Costs Battery for the comm. The character must write it down correctly — there is no save state.
- **Direct observation.** Watching someone enter a code, or finding it written somewhere obvious.

A code is consumed by *use*, not by knowledge. Once known, the character can use it as many times as the door is functional. But a code can become invalid — see Chapter 11 for AI compromise and code wipes.

A code log on the worksheet should track:

- The code itself
- What it opens
- Where the character found it
- Whether it is still valid

When the character is mid-mission and needs to remember which six-digit code opens which lab door, the log is the difference between progress and panic.

## 4.6 Character Clearance

The character's own clearance is determined at character creation, modified by the contract or assignment.
*(See PSG → Classes for class details.)*

Default by class:

| Mothership Class | Typical Default Clearance |
| ---------------- | ------------------------- |
| Teamster         | Crew (White)              |
| Marine           | Crew, sometimes Officer in security contexts |
| Scientist        | Officer (Yellow) in their area, Crew elsewhere |
| Android          | Officer (Yellow), variable by model |

The contract may grant temporary higher clearance. *"You have Officer clearance for the duration of this contract — 72 hours from boarding. After that, your credentials revert."* Temporary clearances are excellent fuel for time pressure.

Some doors will be permanently above the character's clearance. The character will need crew help, codes, or hot-wires for those. This is intentional: it makes the crew genuinely necessary, and it makes Executive sections feel forbidden until they aren't.

## 4.7 The Mislabeled Door

Stations are not perfect. Years of patches, corporate cost-cutting, contractor mistakes, and undocumented modifications mean that some doors do not behave as labeled.

Suggested oracle check at any door: *Is this door as it appears?* Default Likelihood: *Likely*. Modify down for:

- Old infrastructure (-1 step)
- Stations under multiple ownership changes (-1 step)
- Stations under active corporate cover-up (-2 steps)
- Stations in active compromise (-2 steps)

When the answer is *No*, the door is not what its panel claims. Possibilities include:

- Labeled higher clearance, actually opens with lower (corner-cut by maintenance)
- Labeled lower clearance, actually requires higher (re-flagged for security but not relabeled)
- Labeled functional, actually broken
- Labeled to one section, actually opens to another (door reused after section reorganization)
- Labeled secure, actually accessible by manual force (rotted seals, broken hinges)

A mislabeled door in the character's favor is a small gift. A mislabeled door against the character is a betrayal of the systems they thought they understood.

Both increase the sense that the station is alive, broken, and not on anyone's side.

## 4.8 Doors And The Web

Doors are where most of the manual's systems converge. To open a routine clearance-locked door, the character may need:

- Their own clearance, **or** a crew member with clearance
- Working comms (Battery)
- Crew at a working terminal (their section's power)
- Working power in the door's section
- Uncompromised data systems (no AI corruption affecting the door)

When any of these fail, the character chooses between alternate routes, hot-wiring, finding the right code, or waiting.

A station in nominal condition has many open doors and few problems. A station in crisis is a maze of locked doors, each one a small interrogation of how much the character is willing to spend.

---

*Chapter 5 — Power & Section Status — covers the underlying power state that makes most of this work, and what happens when it doesn't.*
