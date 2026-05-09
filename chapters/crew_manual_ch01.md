## 1. INTRODUCTION & CORE LOOP

### 1.1 What This Is

Crew Manual is a solo play supplement for the Mothership Sci-Fi Horror Roleplaying Game. It bolts onto base Mothership rules without replacing them.

It adds:

- A resource economy for batteries, oxygen, ammo, supplies
- A remote crew system — NPC allies who exist over comms, not at the character's side
- Section-by-section tracking for power, integrity, and atmosphere
- Security clearance and access control
- A Station AI with priorities of its own
- Hot-wire mechanics for desperate workarounds
- Station-wide lockdown and emergency protocols

Each system is modular. Use what suits your session. The systems are designed to work together — a failure in one ripples through the others — but each functions on its own.

### 1.2 What You Need

- The Mothership Player's Survival Guide.
- A solo oracle. Mythic Game Master Emulator is recommended. Any oracle works.
- Polyhedral dice including d4, d6, d8, d10, d100.
- The worksheet at the back of this manual. Photocopy it.

### 1.3 How To Run A Session

1. Set up the character per Mothership core rules.
2. Set up the crew (see *Crew & Comms*). Three to five members is standard.
3. Set up the station (see *Sections & Atmosphere*). Sketch sections; mark power, integrity, atmosphere.
4. Define the situation. Why is the crew here? What is the contract?
5. Begin play with the Core Loop (1.4).

### 1.4 The Core Loop

Solo play needs structure. The Core Loop is the rhythm of a scene.

1. **State the situation.** Where is the character? What are they doing? One sentence.
2. **State the question.** What does this scene need to answer? One question.
3. **Resolve.** Use Mothership rules, the systems in this manual, and oracle queries.
4. **Spend resources.** Mark charges, dice rolls, and time on the worksheet.
5. **Note consequences.** What changed? What threads opened or closed?
6. **Set the next question.** What does the character now need, want, or fear?
7. **Repeat.**

When the question is answered, the scene is over. Cut to the next.

If the situation has stalled — no resource being spent, no question pressing, nothing threatening — the Loop has broken. Force movement. Roll a Random Event. Tick the AI's threat assessment. Step a Section's power down a tier. *The Loop is alive only when squeezing.*

The Core Loop above is the per-scene rhythm. Between scenes, the world keeps moving — cascades spread, crew act off-screen, the AI revises its priorities. Run the **Inter-Scene Checklist** (Appendix A.6) at every scene transition to keep these systems alive. For the full Mythic-integrated scene-framing procedure, see *Mythic GME Integration* (Chapter 12).

### 1.5 The Web

The systems in this manual interact constantly. A failure in any node ripples to others.

```
            BATTERY (player)
                 │
         ┌───────┼───────┐
         ▼       ▼       ▼
       LIGHT   COMMS   TOOLS
                 │
                 ▼
               CREW ──→ CLEARANCE ──→ DOORS
                                        │
                                        ▼
                                    SECTIONS
                                        │
                     ┌──────────────────┼──────────────────┐
                     ▼                  ▼                  ▼
                   POWER            INTEGRITY         ATMOSPHERE
                     │                  │                  │
                     └────────┬─────────┴──────────────────┘
                              ▼
                          STATION AI ←─── CORRUPTION
                              │
                              ▼
                          PROTOCOLS
                      (triage, lockdown)
                              │
                              ▼
                    HOT-WIRE (player override at Battery cost)
```

The character spends Battery to act. Comms reaches Crew. Crew has Clearance and Position. Clearance plus working Power opens Doors. Doors gate Sections. Sections each track Power, Integrity, and Atmosphere independently. The Station AI manages Power and reports Integrity — but the AI may be Compromised. Hot-Wire bypasses some constraints at the cost of the character's own Battery.

When something fails, look at the Web. Nothing fails alone.

### 1.6 Quick Reference

*Tear this page out. Tape it where you can see it.*

**Resource Dice.** Each resource is a single die. After meaningful use, roll it.

- On 1 or 2: step the die down (d10 → d8 → d6 → d4 → empty).
- On 3 or higher: no change.
- Empty die: the resource is gone. Effects apply.

| Resource     | Default | Step Trigger | When Empty                |
| ------------ | ------- | ------------ | ------------------------- |
| Battery      | d8      | Charge spent | No light, comms, or tools |
| O2 (EVA)     | d10     | Per EVA scene | Suffocation. Panic.       |
| Ammo         | d8      | After combat | Empty weapon              |
| Stims/Medkit | d6      | After use    | No healing                |
| Rations      | d10     | Per shift    | Hunger. Exhaustion.       |

**Comms.** 1 Charge per call. Oracle: does crew respond? On 1 (d10), Random Event.

**Section States.** Each section tracks three independently.

| Power    | Integrity   | Atmosphere   |
| -------- | ----------- | ------------ |
| Nominal  | Sealed      | Breathable   |
| Brownout | Compromised | Toxic / Thin |
| Dead     | Vacuum      | Vacuum       |
|          | Flooded     | Flooded      |

**Clearance.** White (Crew) → Yellow (Officer) → Red (Executive). Maintenance (Grey) runs parallel.

**Hot-Wire.** Step Battery down one tier, then roll d6:

- 1: Backfire — something unintended.
- 2–3: Wasted — no effect.
- 4+: Success — one action.

Skill modifier: +1 with Engineering or Computers ≥ 40; +2 with ≥ 60.

**AI Stages.** 0 (Clean) → 1 (Drift) → 2 (Irrational) → 3 (Hostile) → 4 (Open).

**Glossary.**

- **Charge.** A unit of Battery use.
- **Cascade.** Failure spreading between adjacent sections.
- **Lockdown.** Station-wide override protocol.
- **Oracle.** Your solo question-answering tool (Mythic GME).
- **Stage.** AI corruption level.
- **Step Down.** Reducing a resource die by one tier.
- **Tier.** AI Power Triage priority level.

---

*[Chapter 2: Resource Dice](crew_manual_ch02.md) covers the foundation system every other system rests on.*
