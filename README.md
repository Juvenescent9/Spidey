# Spidey
A 3x3 macropad designed to resemble a spider

![Image](https://github.com/user-attachments/assets/b56a4f5f-a9c1-4f9b-8d8f-faf50ebb7cd4)

When designing, I took inspiration from the Mercury k1 keyboard made by Gravastar. It is a 9 key macropad, using the XIAO RP2040 microcontroller and powered with KMK firmware. It has 6 articulated limbs that can be adjusted to change the position of the macropad, but mostly because of design preferences. 

# CAD design

The design was fully created in Fusion 360. The case is held by 4 M3 16mm screws, and has 3 plates for the frame. The limbs are made with a ball and socket joint and can allow the macropad to be tilted or even lifted!  _**Although in the CAD file, the limbs are displayed as passing through the framework, when actually built it will be held by printing the limbs individually, and then securing them on accordingly with a 3d pen or hotglue. This is extrememely important for assembly**_ All essential parts of the casing can be printed without supports, except the legs which are not needed for functional reasons and are optional.

![Image](https://github.com/user-attachments/assets/359876ef-45d6-4de2-a8f9-6f2bd9be58ce)

Hackpad without limbs

# PCB
The PCB was made in Kicad. I used a traditional 6 pin system.

![Image](https://github.com/user-attachments/assets/2c63221d-6a3d-43e2-a50c-a795d92e6df6)
![Image](https://github.com/user-attachments/assets/2e6510f1-3655-43f4-b1cc-94aa1f7b8fdd)

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
