# Spidey
A 3x3 macropad designed to resemble a spider

Insert image of it here later. 

When designing, I took inspiration from the Mercury k1 keyboard made by Gravastar. It is a 9 key macropad, using the XIAO RP2040 microcontroller and powered with KMK firmware. It has 6 articulated limbs that can be adjusted to change the position of the macropad, but mostly because of design preferences. 

# CAD design

The design was fully created in Fusion 360. The case is held by 4 m3 s6mm screws, and has 3 plates for the frame. The limbs are made with a ball and socket joint and can allow the macropad to be tilted or even lifted!  _**Although in the CAD file, the limbs are displayed as passing through the framework, when actually built it will be held by printing the limbs individually, and then securing them on accordingly with a 3d pen or hotglue. This is extrememely important for assembly**_ All essential parts of the casing can be printed without supports, except the legs which are not needed for functional reasons and are optional.

Insert image later

Hackpad with and without spider limbs

# PCB
The pcb was made in Kicad.

Insert image here

# Firmware
The hackpad uses KMK firmware. It was my first time using Python apart from FLL, but it proved to be simple

# BOM
Solder, PCB, motivation, and caffeine not included, but required

## Electronic parts
 - 9 DSA keycaps
 - 9 1n4148 diodes
 - 1 XIAO RP2040 (with headers)
 - 9 Cherry MX switches

## Case
 - 4 M3x16mm screws
 - Top part of case
 - Middle part of case
 - Bottom of case
 - 6-8 spider limbs (Optional, number depends on preference)
 - Hot glue (Optional, for grip)
