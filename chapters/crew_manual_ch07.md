# 7. EVA & SUBMERSION OPERATIONS

When a section becomes uninhabitable — Vacuum, Flooded, Toxic, or simply outside the structure entirely — the character cannot enter without a sealed suit and the procedures that come with it. This chapter covers the cost of going outside.

The term "EVA" is used throughout for both true vacuum extravehicular activity and submerged operations underwater. The mechanics are nearly identical; the fictional differences matter, but the procedural answer is the same: seal up, depressurize or pressurize, enter the dark.

## 7.1 What This Chapter Covers

EVA in the Crew Manual is not a quick option. It is a formal process with preparation, execution, and return phases. Each phase has its own resource costs and risks.

A complete EVA scene typically takes one or more in-game scenes to resolve. Plan for it. The character does not casually pop outside.

## 7.2 Suits And Equipment

A working suit is required to operate outside a sealed atmosphere. Suits vary by environment.
*(See PSG → Armor for standard Mothership Vaccsuit and EVA suit specifications.)*

| Suit Type        | Rating                       | Typical Use                       |
| ---------------- | ---------------------------- | --------------------------------- |
| Standard EVA     | Vacuum, light radiation       | Space, lunar surface, low atmosphere |
| Heavy EVA        | Vacuum, heavy radiation, debris | Asteroid work, exterior repair |
| Hazmat           | Toxic atmosphere, biohazard   | Contaminated interior sections    |
| Standard Diving  | Surface to ~200m              | Shallow ocean, lakes              |
| Hardsuit / ADS   | Deep submersion (>200m)       | Deep ocean, pressure floors       |
| Combination      | Mixed (vacuum + cold, etc.)   | Specialty / experimental          |

A suit not rated for the environment will fail. A standard EVA suit in deep ocean is killed by pressure long before O2 runs out. A standard diving suit in vacuum cannot hold pressure inward.

The character cannot improvise their way around suit ratings. The wrong suit means death.

In addition to the suit itself, a typical EVA loadout includes:

- **Helmet** — HUD, comms, lamp, possibly external sensors
- **Tether** — physical line back to a fixed anchor, or a buddy line to crew
- **O2 tank** — primary breathing supply, tracked as O2 die
- **Tools** — limited; gloves restrict fine work
- **Emergency pack** — patches, sealing foam, backup O2 cell

Each of these can be omitted, but each omission becomes a cost the moment it matters.

## 7.3 The EVA Procedure

A standard EVA goes through five phases. Each is its own scene element, though several can resolve in a single scene if simple.

**Phase 1 — Preparation.**

1. Identify the airlock or pressure interface to use.
2. Confirm suit rating matches environment.
3. Check O2 tank: is the die at default? If not, swap or accept reduced operating time.
4. Check Battery: helmet electronics draw on it.
5. Verify comms with crew if they are in scope.
6. Don the suit. Takes 1d6 minutes — typically resolves as a brief beat in the previous scene.

**Phase 2 — Airlock Cycle.**

1. Enter airlock. Seal inner door.
2. Depressurize (vacuum) or pressurize (submersion). Takes 1 to 3 minutes.
3. Listen. Cycling pumps make noise — both for the character and for whatever is on the other side. Whatever lives in vacuum or underwater can sometimes hear airlocks operate.
4. Open outer door.

**Phase 3 — Exterior Operations.**

The bulk of the EVA. Each scene in suit ticks O2 (and Heating, if relevant — see 7.5). The character moves, performs tasks, observes, communicates. Reduced capability rules apply (7.7).

**Phase 4 — Return.**

1. Reach the airlock — ideally the one used to leave, but any working airlock will do.
2. Enter, seal outer door.
3. Cycle. Wait. Cycling time is the same on the return.
4. Open inner door.
5. Doff suit. Return to normal operations.

**Phase 5 — Recovery.**

Suit goes to maintenance or storage. O2 tanks swap or recharge. The character checks for damage they may have ignored while outside.

## 7.4 O2 And Power In Suit

In suit, the character's O2 die ticks each scene of operation. Default starting state is d10. The die is rolled at the end of each scene; on 1 or 2, it steps down.

Heavy exertion — combat, sustained physical work, panic — ticks faster. The Warden, or oracle in solo play, may require an extra roll or step-down for high-exertion scenes.

Battery in suit is not separately tracked — it draws from the character's standard Battery die. Helmet lamp, suit comms, HUD, and any tools all consume Battery as normal. A long EVA can drain Battery faster than O2.

When O2 reaches d4, the character is on their last reserve. Approximately one scene remains before suffocation. Panic Check on emptying.

## 7.5 Heating And Other Environmental Resources

Some environments require additional resource tracking beyond O2.

**Heating** is critical in cold environments — deep space without solar exposure, polar surfaces, deep ocean. In sufficient cold, suit heating runs continuously and represents a separate die (default d8). When heating is exhausted, the suit cannot maintain core temperature; the character faces hypothermia, panic, and equipment failure as suit electronics struggle.

**Cooling** is the inverse — high-temperature environments (volcanic vents, reactor proximity, hostile atmospheres). Tracked similarly.

**Filter** is required for toxic atmosphere operations. A separate die representing the filter cartridge. When exhausted, the suit's air supply is no longer cleanable; switch to sealed O2 only, or evacuate.

Track only the environmental resources that matter for the operation. A vacuum EVA in normal radiation needs O2 only. A deep ocean EVA may need O2, Heating, and Battery all simultaneously.

## 7.6 Suit Damage And Breach

A suit can be damaged. Damage is binary at trivial scales (a scuff is nothing) but rapidly becomes catastrophic at higher levels.

When a suit takes a meaningful impact, abrasion, or contact with a hostile environment hazard, roll 1d6:

- **1: Breach.** Suit integrity is lost. In vacuum, immediate decompression — Panic Check, severe damage, O2 loss accelerates dramatically. Underwater, water enters; in pressurized environments, the character may be killed by pressure differential before drowning matters. Emergency patching may stabilize, but only briefly.
   *(See PSG → Wounds & Damage for damage resolution; PSG → Stress & Panic for Panic Check.)*
- **2 or 3: Compromised.** Slow leak. O2 die steps down an extra step. Heating may also fail. Patching with sealing foam holds for the rest of the scene; permanent repair requires return to a maintenance station.
- **4 to 6: Holding.** No effect.

Patching a compromised suit takes 1d6 seconds and requires sealing foam from the emergency pack. A character with no patches has no recourse — they must reach an airlock immediately.

A breached suit cannot be patched in time except with extraordinary luck. The character must reach pressure within scenes.

## 7.7 Reduced Capability In Suit

A suited character is not their full self.

- **Skill rolls requiring fine motor control suffer a penalty.** Computers, electronics work, surgery, anything requiring delicate manipulation — typical penalty -10 or -20 depending on suit type. Hardsuits are worst.
- **Movement is slower.** A character in heavy EVA or hardsuit cannot run, climb quickly, or change direction sharply.
- **Vision is restricted.** Helmet visors limit peripheral vision. Fog from breath, condensation, or scratches reduce clarity. The lamp shows only what it points at; everything outside the cone is darkness or murk.
- **Hearing is changed.** In vacuum, no ambient sound carries — only what comes through suit comms. Underwater, sound is everywhere but distorted, and direction is hard to judge.

To perform fine work in suit, the character may need to remove gloves — exposing hands directly to the environment. This is suicide in vacuum and dangerous in nearly all other EVA contexts. It is sometimes the only option.

## 7.8 EVA Comms

Comms in EVA work differently than inside a station.

**In vacuum.** Suit radio carries voice. Comms with crew on the station are normal — Battery cost per call, oracle check for response. Range is limited to the station's transmitters. Beyond that, the character is alone with the dark.

**Underwater.** Standard radio does not penetrate water. Comms is by:
- **Hardline / cable.** Physical connection via the tether or a separate comm line. Reliable. Can be cut, severed, or fouled.
- **Hydrophone.** Acoustic signal through water. Range is limited and varies with thermoclines, currents, and depth. Other things in the water can hear it. Other things can also produce sounds that the character mistakes for comms.

A submerged character may use coded ping signals instead of voice — one ping for "OK", two for "trouble", three for "come help". Voice transmission is possible but expensive in clarity and risk.

When EVA comms degrades or fails, the character may not be able to reach the crew at all. This is often the moment when the EVA becomes a horror scene rather than a procedure.

## 7.9 Light And Sound In Hostile Environments

In standard interior operations, the lamp and the voice are tools. In hostile EVA environments, they are *signals*.

**Light** illuminates a cone. Outside that cone, the character cannot see. But anything in the environment — predator, hazard, observer — can see *the light source*. The lamp marks the character's position to anything looking. In deep water this is profound; bioluminescent or visual hunters orient on light. In atmospheric haze, dust storms, or glowing nebulae, similar concerns may apply.

The character can choose to operate without the lamp, navigating by HUD, instruments, or memory. This costs no Battery for lighting but requires operating in darkness or near-darkness, with visual skill checks at penalty.

**Sound** is similar but less controllable. In water, every motion makes noise — fins, suit joints, tools, comms transmissions. The character cannot move silently. But the *amount* of sound can be controlled by moving slowly, using minimal tool work, and refraining from voice comms.

In vacuum, sound does not carry through the medium itself, but vibration through the structure does. A character drilling on a hull plate transmits vibration through the metal that anything attached to that hull can feel.

The Warden, or oracle, may track an awareness or detection level for hostile entities in the environment. Lamp use, sound, and movement increase it. Stillness and dark reduce it.

## 7.10 Exterior As Game Space

A station's exterior is a separate region for navigation purposes. The character operating outside can:

- **Move along the hull.** Slow, with magnetic boots or handholds in vacuum, with fins underwater. Not always continuous — gaps exist.
- **Reach sections inaccessible from inside.** Damaged corridors, sealed-off compartments, locked-down areas. The exterior is sometimes the only route.
- **Observe.** Looking through viewports into the interior. Watching what the character cannot reach. This can be horrifying — seeing crew members through a window, unable to help, unable to be seen. Or seeing things in the sections that should not be there.
- **Access exterior systems.** Antenna arrays, sensor packages, hull-mounted equipment, emergency release valves.

Treat the exterior as one or more sections in its own right. They may have their own hazards and characteristics — radiation belts, fast currents, predator zones, debris fields.

## 7.11 Locked Out

The most acute EVA scenario is being unable to return.

A station that detects an exterior threat may **lock down its airlocks** to prevent the threat from entering. Standard procedure. Not malicious. The station does not always distinguish between threat and crew member.

When the character is outside and lockdown engages:

1. The airlock used to exit no longer cycles in. The character receives a refusal signal at the panel.
2. Comms may be filtered or restricted under lockdown protocol.
3. The character has limited time — measured in O2 and Heating — to find a solution.

Solutions to a lockout:

- **Crew override.** A crew member with appropriate clearance can manually lift the lockdown for a specific airlock. Requires comms, a working terminal, sufficient clearance, and the crew member's willingness given the threat that triggered the lockdown.
- **Emergency airlock.** Most stations have at least one emergency airlock with an exterior manual override. The character must find it. Depending on layout, this may be a long traverse.
- **Hot-wire.** The character can hot-wire an external airlock panel using personal Battery (Chapter 10). The panel may not always be accessible without tools, and noise from the operation is significant.
- **Wait.** Some lockdowns lift when the trigger condition resolves. If the threat moves away or is neutralized, the lockdown ends. The character must survive until then.
- **Distress signal.** Broadcasting on emergency frequencies may bring crew action — but it also broadcasts the character's position to anything listening.

A lockout is the EVA situation that turns a routine exterior task into a survival scenario. The systems built throughout this manual converge on it. The character is alive, in the dark, with a tank of O2 and a battery, and the door will not open.

## 7.12 Stress In EVA

EVA carries baseline Stress. The environment is hostile; the suit is fragile; the dark is large.

| EVA Condition                   | Stress Effect                           |
| ------------------------------- | --------------------------------------- |
| Routine suited operation        | +1 Stress on first scene of each EVA    |
| Suit Compromised                | +1 Stress immediately                   |
| Suit Breach                     | Panic Check immediately                 |
| Lost comms with crew (alone)    | +1 Stress per scene                     |
| Locked out (cannot return)      | +1 Stress immediately, +1 per scene     |
| Operating without lamp (dark)   | +1 Stress per scene                     |
| In view of unknown thing        | +1 to +2 Stress, oracle's call          |

Stress in EVA is not a flat penalty. It is a measure of how close the character is to making the wrong decision in a place where wrong decisions are usually fatal.

A character who has accumulated significant Stress in suit may make a Panic Check that breaks them — running, freezing, or doing something irrational with limited resources. The horror of EVA is not just the environment. It is what the environment does to the people who go into it.

> *See PSG → Stress & Panic for the Panic Check procedure and Panic Effects table.*

---

*Chapter 8 — Station Protocols & Lockdown — covers the formal automated systems that run the station, including the lockdown procedures referenced in this chapter and others.*
