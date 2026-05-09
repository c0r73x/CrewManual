# 10. HOT-WIRE & POWER SACRIFICE

When clearance fails, codes are wiped, crew can't be reached, and the AI says no — the character has one tool left. They can connect their own power source directly to a system and force it to operate. The cost comes out of their Battery permanently.

This chapter covers the hot-wire mechanic in detail. It is the only system in this manual that lets the character bypass the others. It is also the only system that consumes a character resource without rolling for it.

## 10.1 What Hot-Wiring Is

A hot-wire is a direct power connection from the character's portable battery to a target system. It bypasses normal authorization. It does not care about clearance, codes, AI permissions, or station power state. It only cares whether the system itself is physically intact.

A hot-wire is one of the few actions the character can take that the station cannot prevent. Locked doors, dead terminals, dark comms relays — all of them have power inputs. Connecting one's own power to those inputs makes the system attempt to function.

Hot-wires are not subtle. They are physical work — exposed panels, tools, raw cables. They are also limited. A hot-wire produces one action: open this door, light this terminal, send this transmission, run this device for one scene. The character cannot hot-wire a sustained operation.

## 10.2 The Procedure

To hot-wire a system:

1. **Identify the target.** A specific door, terminal, comms relay, life support panel, lock mechanism, or other discrete system. The target must be physically accessible — the character can reach the panel, expose the wiring, attach connections.
2. **Step the Battery die down one tier.** No roll. The cost is immediate and permanent for this session.
   - d10 → d8 → d6 → d4 → empty
   - If Battery is empty, the character has no power to share. Hot-wire is impossible.
3. **Roll 1d6** to determine the result. Apply skill modifier if the character has Engineering or Computers (typical: +1 with skill ≥ 40, +2 with skill ≥ 60).
   *(See PSG → Stats & Skills for skill values and check resolution.)*
4. **Resolve:**
   - **1: Backfire.** The hot-wire produces an unintended consequence. Oracle decides what (10.5).
   - **2 or 3: Wasted.** Battery is gone, system did not respond. The character may try again — at further cost.
   - **4 or higher: Success.** The system performs one action.

A successful hot-wire is one action. Not two. Not "for as long as it takes." If the character wants to keep a hot-wired terminal lit longer than one scene, they hot-wire it again — at further cost.

## 10.3 What Can Be Hot-Wired

Most discrete electrical systems with accessible power inputs:

- **Doors.** Open or close once. Doors locked by clearance or code can be opened. Doors locked by Total Lockdown require additional effort (often two hot-wires — one to bypass the lockdown lock, one to actuate the door).
- **Terminals.** Light up a dead terminal long enough to read what's on it, attempt one operation, or download a small amount of data.
- **Comms relays.** Send one transmission through a dark relay. The character must know the destination and the message must be brief.
- **Life support panels.** Run a single function — purge atmosphere, vent, restore circulation — for one scene. Useful for clearing toxic atmosphere from a small space.
- **Locks and physical security devices.** Defeat a single mechanism. Useful for biometric locks where the original key-holder is dead.
- **Sensors.** Activate a single sensor pass — read what is in this room, what is in this corridor, what is the atmospheric composition here.
- **Tools and devices.** Run a portable device that has lost its power source.

The general rule: if a system has a defined function and an accessible power input, it can probably be hot-wired.

## 10.4 What Cannot Be Hot-Wired

Some things the character cannot hot-wire, no matter how much Battery they sacrifice:

- **Mechanical systems** with no electrical component. Sealed bulkheads with hand cranks. Pure mechanical valves. These require physical force or proper tools.
- **Systems with multiple coordinated components** where hot-wiring one is not enough. The character cannot hot-wire a reactor restart — too many simultaneous systems are involved.
- **Damaged systems** where the underlying device is broken, not just unpowered. A hot-wire provides power, not parts. A burned-out motor will not turn even if energized.
- **Systems where the power input is destroyed.** If the panel is melted, broken, or sealed inaccessibly, there is no input to connect to.

The Warden, or oracle, decides when these conditions apply. The character may not always know in advance. A failed hot-wire that produces "Wasted" rather than "Success" may be the system telling the character that this thing cannot be hot-wired — without saying so directly.

## 10.5 Backfire

A 1 on the d6 indicates a backfire. The hot-wire produces unintended consequences.

The oracle determines the specific backfire. Suggested backfire types:

| Backfire Type            | Effect                                                                 |
| ------------------------ | ---------------------------------------------------------------------- |
| Triggered Alarm          | A nearby alarm activates. Crew, AI, or hostile forces are alerted.     |
| Triggered Sensor         | Adjacent sensors register the hot-wire as anomalous activity. Investigation may follow. |
| Wrong Door               | A different door than the target opens, often elsewhere in the section. |
| System Damage            | The target system is damaged in addition to being unsuccessful. May lock permanently. |
| Cascade                  | The hot-wire triggers a power cascade. Adjacent section drops one tier of Power. |
| Fire / Sparks            | Electrical fire or significant arcing. Fire suppression may activate. The character takes damage. |
| Crossed Signal           | An unrelated system activates instead — random door opens, alarm sounds, sensor activates. |
| Identification           | The hot-wire's signature is logged by the AI or external monitoring. Consequences may follow later. |

A backfire does not necessarily prevent further attempts. The character may try again — at the cost of another tier of Battery — though the consequences of the first backfire may make the situation worse.

## 10.6 Tools And Skill

Hot-wiring requires tools. A standard maintenance multitool, electrician's kit, or technician's pack will do. A character with no tools cannot hot-wire — they have nothing to connect with.

Tools may be lost, broken, or left behind. A character separated from their pack faces hot-wires without their primary equipment. They may improvise (the oracle decides whether and at what cost) but cannot perform reliable hot-wires.

Skill modifies the hot-wire roll:

| Character Has         | Modifier to 1d6 |
| --------------------- | --------------- |
| Engineering ≥ 40      | +1              |
| Engineering ≥ 60      | +2              |
| Computers ≥ 40        | +1 (terminal/sensor hot-wires only) |
| Both at high skill    | Use higher; do not stack |

A character without relevant skill rolls without modifier. A failed hot-wire by an unskilled character is more likely; the system is not for amateurs.

## 10.7 Time And Noise

A hot-wire is not instant. It takes time and produces noise.

**Simple hot-wires** (a door, a single terminal): one minute of work. Resolves within a single scene.

**Complex hot-wires** (a comms transmission, a life support panel): three to five minutes. The character is committed for that duration; interruption may abort the attempt and waste the Battery cost without effect.

**Noise level** depends on the work. Stripping cable, exposing panels, and connecting power produces sound. In quiet environments, this is heard. In hostile environments — with predators, hostile crew, or watching things — the noise is a beacon.

A character hot-wiring while pursued has chosen to commit to the action. They cannot hot-wire and run at the same time. They are stationary, hands occupied, attention focused. Whatever was approaching is still approaching.

## 10.8 Crew Hot-Wires

Crew members can also hot-wire systems. They do not have a personal Battery die in the same way, but they can sacrifice their station's resources for the character's benefit.

**Procedure for crew hot-wire:**

1. Character requests via comms (1 Charge for the call).
2. Crew member confirms feasibility — they must be at a relevant access point and have appropriate skill.
3. Crew sacrifices a portion of their station's reserve power. The crew member's section may drop one Power tier as a result.
4. Roll 1d6 with crew member's skill modifier. Resolve as normal.

A crew hot-wire is a powerful tool. It lets the character bypass a problem without spending their own Battery. But it costs the crew, and it costs the section they are in.

> *EXAMPLE.* The character is at a Yellow-clearance door. They have no clearance, no code, and Battery is at d4 — too low to risk a personal hot-wire. They call Voss, who is at engineering. Voss agrees. Voss connects engineering reserve power to the door's circuits. Engineering drops Brownout. Voss rolls Engineering: 5 with skill modifier. Success. The door opens. The character passes through. Engineering will be in Brownout for the rest of the scene at least.

Crew hot-wires also have backfire potential. A backfire affects the crew's section — fire in engineering, alarm at the bridge — and may put the crew member in immediate danger.

## 10.9 Hot-Wire And The Web

Hot-wire is the player's primary tool for solving problems the rest of the manual creates. It is intentionally costly. The character cannot hot-wire their way through a session — they will run out of Battery.

The systems work together as follows:

- When **clearance** fails: hot-wire the door.
- When **codes** are wiped: hot-wire the lock.
- When **comms** is dark in a section: hot-wire a relay for one transmission.
- When **AI** denies a request: hot-wire the system the AI controls.
- When **power** is dead in a section: hot-wire individual devices to function temporarily.
- When the **station is locked down**: hot-wire an exterior airlock panel.

Each of these is one action. The character chooses where to spend their Battery. They cannot do everything. They must prioritize.

This is the pressure the manual is designed to produce. Survival is not about having every tool work every time. It is about choosing which tool to use *now*, knowing that future scenes will need tools too, and that every choice forecloses something.

---

*Chapter 11 — System Compromise — covers what happens when the systems themselves cannot be trusted: virus, memory wipe, AI corruption, and the slow loss of certainty.*
