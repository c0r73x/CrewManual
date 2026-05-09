# 2. RESOURCE DICE

Resource Dice are the foundation of this manual. Every other system in this book either consumes a resource, threatens one, or rewards careful management. Understand this chapter and the rest follows.

## 2.1 The System

Each tracked resource is represented by a single polyhedral die. The size of the die represents the abundance of the resource. A larger die means more left.

After meaningful use, the die is rolled.

- On a roll of **1 or 2**, the die *steps down*: d10 → d8 → d6 → d4 → empty.
- On a roll of **3 or higher**, no change.
- When the die is empty, the resource is gone. The corresponding effect applies.

The system abstracts the bookkeeping. The character does not count individual rounds, charges, or rations. They estimate. The die is their estimate.

> *EXAMPLE.* The character has a Battery die at d8. They use the radio to call the engineer. Roll d8: a 5. No change. Later they hot-wire a door, which steps the Battery down without rolling. Battery is now d6. Two scenes later they spend another charge on a tool. Roll d6: a 2. Step down to d4. The character notices the indicator light has dropped into the yellow.

## 2.2 When To Roll

Roll the die *after* the action that used the resource — not before. This means the action always succeeds at the cost of a chance the resource degrades. The die is not a permission. It is a consequence.

Roll the die when:

- A **charge** is spent (Battery, O2, etc).
- A **scene ends** in which the resource was actively in use.
- A **shift ends** for resources tracked over time (Rations, water).
- An **explicit step-down** is required by another system, in which case do not roll — just step down.

Do not roll for trivial use. A Battery is not stepped down by checking the time on a wrist display. It steps down for sustained use of a tool, lamp, or comm transmission.

## 2.3 Step-Down Cost

Stepping down does not happen often, but when it does, it is permanent for the session. The character cannot recover a stepped-down resource without finding more — a charging station, a med locker, an ammo cache, a ration crate. These are not free. They are scenes.

When a die reaches **d4**, the character is on the brink. The next failed roll empties it. In a horror context, this is where the squeeze begins: rationing, prioritizing, hot-wiring instead of using normally to avoid further rolls.

When a die is **empty**:

- **Battery:** No light, no comms, no powered tools. The character is dark.
- **O2:** Suffocation. Panic Check. Critical timer.
- **Ammo:** Weapon empty. Reach for a sidearm or run.
- **Stims/Medkit:** No healing. Wounds bleed.
- **Rations:** Hunger sets in. Within a shift, exhaustion. Within two, panic.

## 2.4 The Five Standard Resources

### Battery (default d8)

Powers everything the character carries. Lamp, comms, scanner, powered tools, EVA suit electronics. Most actions in this manual cost Battery charges.

A charge is one use: one comm transmission attempt, one tool activation, one scene of active lamp use, one hot-wire attempt at the cost of a step-down.

Battery is the resource the character feels most acutely. Its depletion changes what is possible.

### Oxygen (default d10, EVA only)

Tracked only when the character is in vacuum, hostile atmosphere, or sealed in a suit for extended duration. Outside of EVA, atmosphere is handled by Section state (see *Sections & Atmosphere*).

O2 steps down per scene in suit. A long EVA — repairing a hull plate, traversing a flooded section, exterior navigation — burns through a full tank quickly.

When the O2 die is at d4, the character has perhaps one scene before suffocation. When empty, Panic Check immediately.

### Ammunition (default d8, per weapon)

Tracked separately for each weapon the character carries. A pistol and a shotgun have separate Ammo dice. Use the dice as estimates of remaining magazines or shells, not individual rounds.

Step the Ammo die after any combat scene in which the weapon was fired. Critical fire — emptying a magazine, sustained suppression — steps it without rolling.

### Stims / Medkit (default d6)

Covers all field medical resources. Stim packs, painkillers, bandages, sealing foam.

Step after each use. The default is d6 because medical supplies are rare and limited. A character planning an extended operation should secure additional supplies before deployment.

### Rations / Water (default d10)

Tracked over shifts rather than scenes. A shift is approximately eight hours of operation, or whatever interval the table is using.

Step the Rations die at the end of each shift. The character does not need to actively eat for the die to track — it represents accumulated consumption. When the die approaches d4, the character is rationing visibly. When empty, hunger and dehydration begin to affect performance.

## 2.5 Custom Resources

Specific scenarios may need additional resource tracks. Suggested examples:

- **Coolant** for a reactor that the character must keep stable.
- **Reagents** for a chemistry-based investigation.
- **Power Cells** for a heavy weapon or specialty tool.
- **Adrenaline** as an abstract psychological resource representing peak alertness.

Pick a default die size based on abundance. d10 for plentiful, d8 for standard, d6 for limited, d4 for nearly gone.

Track no more than seven resources at once. Beyond that, the worksheet becomes the game.

## 2.6 Stress Integration (optional)

When a resource die steps down to d4 or empties, the character may take Stress.

- **Stepping to d4:** +1 Stress. The character notices they are running low.
- **Emptying the die:** Panic Check at the new Stress total.

This rule binds resource attrition directly to Mothership's psychological damage system. Use it when a session needs more pressure. Skip it when resource attrition alone is enough.

> *See PSG → Stress & Panic for the full Panic Check procedure (roll d20 under current Stress).*

## 2.7 Replenishment

Resources are recovered by finding more — not by resting.

- **Battery:** Charging stations in safe rooms. Captain's quarters, engineering bays, life pods. Charging takes time (10+ minutes) during which the character is stationary and vulnerable.
- **O2:** Tank swaps at airlocks or O2 lockers. Quick (1 minute) but requires the right station.
- **Ammo:** Caches, fallen marines, weapon lockers. Often clearance-locked.
- **Stims/Medkit:** Med bays, infirmaries, first aid stations.
- **Rations:** Galleys, mess halls, emergency caches. Usually crew-clearance.

Recovery is never free. Reaching a charging station may require traversing a compromised section, opening a locked door, or trusting that the room is empty. The act of recovery is itself a scene.

A recovered resource resets to its default die size, not higher. A character cannot stockpile beyond the default. They carry what they carry.

The summary above covers the broad strokes. *Resource Recovery* (Chapter 14) details multiple recovery methods for each resource, with their access requirements, time costs, and consequences.

## 2.8 Resource Dice And The Crew

The crew has its own resource state, tracked abstractly by the character. The crew does not roll dice. Instead, when the character contacts crew, the oracle determines whether the crew is in good standing or strained, and crew members may report shortages.

> *EXAMPLE.* The character calls the bridge to ask for a sensor sweep. The oracle returns a complication: the bridge reports "running on reserve power, sweeping costs us." The character now knows that any further request to the bridge has a cost. The crew's resources are degrading off-screen.

Crew shortages create scene pressure without adding more dice to the worksheet. The character is told. They cannot verify.

See *Crew & Comms* for the full crew resource framework.

---

*Chapter 3 — Crew & Comms — covers the remote crew system that depends on this resource economy.*
