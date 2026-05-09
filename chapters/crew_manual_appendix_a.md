# APPENDIX A — WORKSHEET & PROCEDURES

The systems in this manual produce a lot of state. The worksheet is where that state lives. It is the player's only reliable record — the thing the AI cannot quietly rewrite, the thing the corruption cannot reach, the thing the character carries out of the dark.

This appendix provides the worksheet templates referenced throughout the manual, plus the Inter-Scene Checklist (A.6) that keeps the world moving between scenes.

Photocopy the worksheets. Write in pencil. Strike through, do not erase, when something becomes invalid — the strike-through is itself a record.

## A.1 Resource Track

One row per tracked resource. Circle the current die size. Step left when the die steps down. Empty when the d4 fails.

```
RESOURCE         CURRENT DIE              STATE / NOTES
------------     -------------------      -------------------------
Battery          d10  d8  d6  d4  ☐       _______________________
O2 (EVA only)    d10  d8  d6  d4  ☐       _______________________
Ammo (weapon 1)  d10  d8  d6  d4  ☐       _______________________
Ammo (weapon 2)  d10  d8  d6  d4  ☐       _______________________
Stims / Medkit   d10  d8  d6  d4  ☐       _______________________
Rations / Water  d10  d8  d6  d4  ☐       _______________________
Heating (suit)   d10  d8  d6  d4  ☐       _______________________
Filter (suit)    d10  d8  d6  d4  ☐       _______________________
Custom: _______  d10  d8  d6  d4  ☐       _______________________
Custom: _______  d10  d8  d6  d4  ☐       _______________________
```

Heating and Filter are tracked only when the EVA environment requires them (see 7.5). Rations are tracked over shifts, not scenes. All others step per Chapter 2.

**Emergency packs carried.** Tally marks. Each pack restores Battery one step (14.2) or O2 one step (14.3). Single use.

```
Battery Emergency Packs: _________________
O2  Auxiliary  Tanks:    _________________
Sealing Foam Patches:    _________________
```

## A.2 Crew Roster

One row per crew member. Three to five rows is standard.

```
NAME      ROLE         STATION (DEFAULT)    SKILLS         STRESS    STATUS
------    ----------   ------------------   ------------   -------   ----------
______    __________   __________________   ____________   Steady    On station
______    __________   __________________   ____________   Strained  Moved to ___
______    __________   __________________   ____________   Breaking  Silent
______    __________   __________________   ____________   Lost      Dead
______    __________   __________________   ____________   _______   __________
```

Update STATION in pencil when the crew member moves. Mark STATUS as **Silent** when a crew member fails to respond (3.8); leave them Silent until verified one way or the other. STRESS is what the player infers from voice and behavior — the character does not see exact values.

## A.3 Section Map

Sketch the station as a node graph. Each node is a section; each line is a connection. Mark connections as **interior** (single line) or **transit** (double line — requires EVA per 6.4).

For each section, track three states:

```
SECTION NAME      POWER          INTEGRITY      ATMOSPHERE
-------------     ----------     -----------    -------------
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
______________    Nom Brn Dead   Sld Cmp V/Fl   Brth Tx V/Fl
```

Circle current state per column. *Nom* = Nominal, *Brn* = Brownout, *Dead*. *Sld* = Sealed, *Cmp* = Compromised, *V/Fl* = Vacuum or Flooded. *Brth* = Breathable, *Tx* = Toxic/Thin.

**Recovery anchors.** Mark each section that contains a known recovery point (per 14.1):

```
SECTION             RECOVERY TYPE              CLEARANCE     LAST KNOWN STATE
----------------    -----------------------    ----------    -----------------
______________      Recharge Station           ___           ____________
______________      O2 Locker / Airlock        ___           ____________
______________      Med Bay / First Aid        ___           ____________
______________      Galley / Mess              ___           ____________
______________      Ammo Cache                 ___           ____________
______________      ________________________   ___           ____________
```

When the character confirms a recovery point exists somewhere, write it down. When that section's state changes such that the recovery point becomes inaccessible (Dead power for a Recharge Station, lockdown sealing a Med Bay), update the LAST KNOWN STATE column.

## A.4 Code Log

Per 4.5. Strike through when invalidated (4.5, 11.7).

```
CODE          OPENS                       FOUND AT             VALID?
----------    ------------------------    -----------------    -------
__________    ________________________    _______________      Y / N
__________    ________________________    _______________      Y / N
__________    ________________________    _______________      Y / N
__________    ________________________    _______________      Y / N
__________    ________________________    _______________      Y / N
__________    ________________________    _______________      Y / N
__________    ________________________    _______________      Y / N
__________    ________________________    _______________      Y / N
```

When System Compromise is in play and a wipe occurs, strike codes through with a single line — do not erase. The character remembers having had them.

## A.5 Comms Log

Per 3.9. One line per exchange. Brief — radio chatter, not novel-writing.

```
SCENE   TIME    IN (crew → character)               OUT (character → crew)
-----   -----   --------------------------------    ----------------------------
_____   _____   ________________________________    ____________________________
_____   _____   ________________________________    ____________________________
_____   _____   ________________________________    ____________________________
_____   _____   ________________________________    ____________________________
_____   _____   ________________________________    ____________________________
_____   _____   ________________________________    ____________________________
_____   _____   ________________________________    ____________________________
_____   _____   ________________________________    ____________________________
```

Continue on a separate sheet for long sessions. The log is the diegetic record of remote contact; preserve it.

## A.6 Inter-Scene Checklist

Run this checklist at every scene transition. The Core Loop (1.4) is the rhythm of a scene; this is the rhythm between scenes. Without it, the world stops moving when the character is not looking — and that is not the world this manual builds.

Work through the items in order. Each is fast. Most will resolve as "no change" most of the time. The point is that none are skipped.

**1. Tick resources for elapsed time.**
- If a shift has ended, roll Rations / Water (2.2).
- If the character was in suit, roll O2 for the EVA scene that just ended (7.4). Heating / Filter dice if tracked.
- If the character was actively using a tool, lamp, or comms during the scene, the relevant Battery roll happens here.

**2. Advance any active cascades.**
- For each section currently Dead, roll 1d6 against each adjacent section that has not already dropped (5.5). On a 1, that section steps down one Power tier. Apply.
- For each section currently Vacuum or Flooded, roll 1d6 against each interior-connected adjacent section (6.6). On a 1, that section drops one tier in Integrity (and Atmosphere where relevant). Apply.
- A cascade resolved this turn does not roll again until the next inter-scene check.

**3. Tick Compromised sections.**
- For each section the character has been in this scene that is Compromised, roll 1d10 (6.9). On a 1, the compromise widens — the section drops to Vacuum or Flooded.

**4. Resolve crew off-screen action.**
- For each crew member who was given an off-screen task (3.3), check whether they have completed it. If the task takes time, narrate progress; if it is done, resolve and report.
- For each crew member out of contact for two or more scenes, oracle: *Has [name] moved?* (12.4). Update Crew Roster.

**5. Check AI behavior.**
- If conditions have changed such that AI Power Triage should re-evaluate (a section dropped, a reactor fault, a new alarm), re-run the priority hierarchy (9.2) and apply.
- If a protocol's trigger condition is now active, fire the protocol (Chapter 8).
- If a protocol's trigger condition has cleared, the protocol may auto-lift per 8.3 / 8.5 / 8.7.

**6. Roll for System Compromise progression (if in play).**
- Per 11.3, either roll the random-progression d100 at the appropriate cadence, or check whether trigger-based progression has crossed a threshold this scene. Advance the AI Stage if indicated. Do not tell the player which stage; the Warden — or in solo play, the player wearing the oracle hat — tracks privately.

**7. Update Chaos Factor.**
- Per Mythic GME rules, adjust Chaos based on whether the previous scene resolved with the character in greater or lesser control. The Crew Manual's suggested trajectory (12.5) gives anchors.

**8. Check for Random Event triggers.**
- Roll Mythic's standard Random Event check at the new Chaos Factor.
- If the previous scene ended with a Comms 1, a hot-wire backfire, or any other manual-specified trigger, roll on the relevant Chapter 13 table now.

**9. Frame the next scene.**
- State the situation. State the question. Apply Mythic's Scene Roll (12.7) — does the scene proceed as expected, alter, or interrupt?
- Begin the Core Loop.

If the checklist surfaces no changes, the next scene begins from a stable state — which is rare, and worth noting. If the checklist surfaces three or more changes, the world has moved significantly while the character was occupied. That is the manual working as intended.

## A.7 Session Setup Sheet

Use once per session, before play begins.

```
STATION NAME:           ____________________________________
OWNER / OPERATOR:       ____________________________________
LAYOUT TYPE:            Single complex / Multi-structure (interior) /
                        Multi-structure (transit) / Mixed
ENVIRONMENT:            Vacuum / Deep ocean / Hostile planet / Other ________

CHARACTER:              ____________________________________
CLASS:                  ____________________________________
DEFAULT CLEARANCE:      White / Yellow / Red / Maintenance
TEMPORARY CLEARANCE:    ____________________  Expires: __________

CONTRACT / SITUATION:
   ___________________________________________________________
   ___________________________________________________________
   ___________________________________________________________

ACTIVE PROTOCOLS:       Lockdown / Quarantine / Evacuation / Reactor Scram /
                        Fire Suppression / Atmospheric Purge / Comms Black /
                        Power Triage / Custom: ________________________

SYSTEM COMPROMISE:      Not in play / In play, Stage ___ (private)
PROGRESSION METHOD:     Random (d100) / Trigger-based / Off

INITIAL CHAOS FACTOR:   _____  (4 default; see 12.5)

RECOVERY ANCHORS KNOWN AT START:
   ___________________________________________________________
   ___________________________________________________________
```

The session sheet is the snapshot of *what the table has decided is true* before the first scene. Everything else is what the dice and the oracle do to that state.

---

## A.8 Afterword

This manual is a list of ways for things to go wrong, organized by system. That is what it is for. It does not tell stories. It produces the conditions in which stories happen — power failing, crew falling silent, doors that should open and don't, batteries that run down faster than expected, an AI making a decision the character doesn't understand for reasons the character will only piece together hours later, if at all.

Solo play with this manual is not about winning. There is rarely a clean win available. It is about the texture of decisions made under constraint: which resource to spend, which crew member to call, which section to traverse, which door to leave locked. Each decision forecloses something. The session is the accumulation of those foreclosures, written down in pencil on a worksheet, until the character finishes the contract or the contract finishes the character.

The systems are designed to fail in connected ways. A Battery shortage limits Comms, which limits Crew, which limits Clearance, which limits Doors, which limits where the character can go to recover Battery. A station whose AI has begun to drift will report that recovery anchor as Nominal up until the moment the character arrives and finds it Dead. The Web in 1.5 is not a chart. It is the shape of how the character runs out of options.

The worksheet is the thing the corruption cannot reach. Whatever the AI tells the character, whatever the crew reports over the radio, whatever the station sensors say — the worksheet is what the player has written down in their own hand, and it is the only record that survives the session. Keep it close. Strike through, do not erase. When something on the sheet stops being true, the strike-through is the proof that the character once thought it was.

That is the genre's promise, restated: in the deepest dark, the analog things still work.

Good luck out there.

---

*This is the end of the Crew Manual. Return to Chapter 1 when ready to begin a new session.*
