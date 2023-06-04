A Text-based Progression Tree
=============================

Trying to implement the (used) progression tree into [GraphML Editor](https://actuallyfro.github.io/Break-FAST/Examples/01_GraphML-Editor/Single-page-Apps/)... maybe.

A Soure
-------
From u/AhCrapItsYou [Progression Tree](https://www.reddit.com/r/spaceengineers/comments/n7ih2g/progression_tree_reference/)

![A 2021 Capture of the Progression Tree](./Progression_Tree.jpg)

The Code
--------
Uses [PlantUML](https://plantuml.com/) to render as a [Work Breakdown Structure (WBS) or 'Org Chart'](https://plantuml.com/wbs-diagram) diagram.
Alternatively, use PlantText.com to edit the [WBS](https://plantuml.com/wbs-diagram) diagram; an [example](https://www.planttext.com/?text=fLF1Zfj03Btp5JvcnIzKrKAIqgsIDYAHeghgmG67dUumWpnce_txcWnamrxtDdv-s7xFvZ48ibnE8Kd4Y2NOTrWHh5rZ7147MEpxKo1vW1txXYa4unqSc2X9qdiiILF8CPWAiX2eFLbYXGPCXFXjUAUmz4xOMzYX8nkXRxvdo7iHBNk5OL6mxxi7-FEqWdATRU1djbt_ZUoT2GDnf4IizE9v3dqthg4vjCIM6ECx9wok4mz1veISYnaDDnY89n0YVszDhHLXvUUDO4krgT3g2BwzSc5ZccU1HNFNMKtwHvNE6CF8o953Z0kB8OpIZyRL_Z8czkI2zhiLQHZR5jLOoAslNY9-C2hh7PYRhmCQNOv-SUYPISQ6A7PGK_IJ1Ikg_BYXVKTKmzRNlVrWuCvVj5FCHEIt8LlFa8BnrSWR5EJKx4bo2Z_wjeCLcrUQJ6SnPrCPzMwhyfERBnctVjHprnwUT1ziD7D4QsShs61TZwUsHBcWVRdQ1oMsNNpfKAAQfkpjlhuSaS_8zFNzT4iwwzd7QuLVJEgCt5Ot2B0s5XzvSuS-vrsfH_dna5FLoy-4TP8yaglrD_qF).

```PlantUML
@startwbs

title Space Engineers (Subset) Progression Tree

+ Progression
++ Basic Assembler
+++ Battery
++++ Control Panel
++++ Four Button Panel (Group) [ID REAL NAME]
++++ Piston (Group)
++++ Rotor (Group)
++++ Hinge (Group)
++++ Camera
++++ Beacon
+++++ Antenna
++++++ Laser Antenna 
++++ Sliding Door (Group)
+++ Medical Room 
+++ Light (group)
++++ Projector
++++ Light Bars
++++ Glass Panel Windows
++++ Sensor 
++++ Programmable Block
++++ Timer Block
+++ Assembler
++++ Missile Turret
++++ Gatling Gun
+++++ Decoy
++++ Speed Module (Group)
++++ Power Module
++++ Yield Module
++++ Gravity Generator
+++++ Jump Drive
+++++ Artificial Mass
++ Light Armor Block (Group)
++ Interior Wall (Group)
+++ Ladder
+++ Catwalks
+++ Ramps
+++ Grated Catwalks (Group) <Warfare>
++ Basic Refinery
+++ Ore Detector
+++ Drill
+++ Refinery (Group)
++++ Speed Module (Group)
++++ Power Module
++++ Yield Module
++++ Reactor (Group)
+++++ Warhead
++ Landing Gear (Group)
+++ Seat
+++ Wheels (Group)
+++ Parachute
+++ Flight Seat (Group)
+++ Cockpit (Group)
++++ Small Grid Gatling Gun
++++ Thrusters Atmospheric (Group)
++++ Thrusters Hydrogen (Group)
++++ Thrusters Ion (Group)
++++ Gyrscope
++++ Grinder (Group)
++++ Welder
++++ Drill
++++ Small Grid Rocket Launcher
++ Oxygen Farm
++ H2/O2 Generator
+++ Oxygen Tank (Group)
+++ Cryo Chamber
+++ Air Vent
+++ Hydrogen Engine 
++ Cargo Container (Group)
+++ Small Grid Conveyor (Group)
+++ Conveyor (Group)
++++ Collector (Group)
++++ Connector
++++ Ejector
++++ Small Grid Connector
++++ Conveyor Sorter
++ Solar Panel
++ Wind Turbine
+++ Merge Block
@endwbs
```