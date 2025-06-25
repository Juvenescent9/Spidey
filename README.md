# Spidey
A 3x3 macropad designed to resemble a spider

![screenshot]([Images/21.27.37.png](https://github.com/Juvenescent9/Spidey/blob/main/Images/Screenshot%202025-06-24%20at%2021.27.37.png)) 

When designing, I took inspiration from the Mercury k1 keyboard made by Gravastar. It is a 9 key macropad, using the XIAO RP2040 microcontroller and powered with KMK firmware. It has 6 articulated limbs that can be adjusted to change the position of the macropad, but mostly because of design preferences. 

# CAD design

The design was fully created in Fusion 360. The case is held by 4 M3 16mm screws, and has 3 plates for the frame. The limbs are made with a ball and socket joint and can allow the macropad to be tilted or even lifted!  _**Although in the CAD file, the limbs are displayed as passing through the framework, when actually built it will be held by printing the limbs individually, and then securing them on accordingly with a 3d pen or hotglue. This is extrememely important for assembly**_ All essential parts of the casing can be printed without supports, except the legs which are not needed for functional reasons and are optional.

Insert image later

Hackpad with and without spider limbs

# PCB
The PCB was made in Kicad. I used a traditional 6 pin system.

Insert image here

# Firmware
The hackpad uses KMK firmware.

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
 - 3d pen (Optional, for securing limbs)
 - Hot glue (Optional, for grip)
