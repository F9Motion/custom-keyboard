# Hi Let's do custom keyboard what don't have anyone!
# September 22: Time to do PCB
For PCB I used SW_Push, 1N4148 diode, RGB diode, OLED Display and raspberry pi pico. Of course, not everythink is easy. My concrete problem is not enought pins as always. I had this problem in keeb too! I just say "I fix this problem tomorrow" and went to sleep.
**Total Spent time: 01:07:14** ~~1 hour 7 minutes 14 seconds~~
<img width="771" height="814" alt="Снимок экрана 2026-09-29 194951" src="https://github.com/user-attachments/assets/3910797e-2cc7-41d7-91c7-d015d0ce1ad4" />
<img width="1421" height="575" alt="Снимок экрана 2026-09-29 194942" src="https://github.com/user-attachments/assets/7625f06e-a071-4bb7-9374-3dc9a63b3160" />

# September 23: I resolved the problem, but at what cost?
This is very irritably problem, so to save my nevres I just delete the OLED display and RGB diode. If only everythink was simple like I mind... Of course NO and only **NO**. In PCB only buttons and diodes and nothink more! But not enought pin with only button and diodes! I asked about this problem to Ai but it can't give me ideas what can fix this problem! So I place ROW in right place too and delete COL10-20 and just restart the numbering form 1-10. I don't know what I did yet but after this plate need only 22 pins it's perfect for Raspberry Pi Pico! I assign the footprint and opened PCB editor mode. I replace all buttons (SW_Push es) and diodes to keyboard form. At work I edit footprint in buttons like space bar ctrl alt tab etc. Because This buttons are bigger than others so I opened Schematic and "refootprint" buttons. I cutted PCB in edge cuts layer and add holes and do tracing from diodes and buttons to pico. I don't finish tracing
**Total Spent time: 02:51:21**
<img width="1574" height="735" alt="PCB" src="https://github.com/user-attachments/assets/33bda796-f185-4ee8-9170-e86f92871b7e" />

# September 24: Doing Case
New day new details for keyboard!
I finish the tracing and did case for keyboard. And that's all. Oh, I forget I put a fair amount of effort into the stage of adding 3D models to KiCad. I spent much time to just add 3d models. Models form grabcad didn't want show in 3d viewer and the bottom line is, I wasted all that time, yet the model still didn't get added.
So I just 1 model for 1 button to just see in blender. In blender I don't do somethink very hard. Case is only cube with hole for PCB no less no more.
**Total Spent time: 00:35:08**
<img width="1297" height="772" alt="Снимок экрана 2026-09-29 195045" src="https://github.com/user-attachments/assets/657806ca-db86-4a11-b4cf-8271bad99ee7" />

# September 25: Writing firmware
At first we add time, board etc. To do this in python we write just import time, import board etc. Nothink hard. Than we write what have to do ROW GPIOS COL GPIOS and ROW pin in COL GPIOS and COL GPIOS in ROW GPIOS. Than writing a keymap. I just write what every button have to do when it pressed.

In short: firmware needed to explain pico what that have to do when which button pressed
I do many mistaked and Ai helped me fix this mistakes.
<img width="797" height="584" alt="Снимок экрана 2026-10-02 224113" src="https://github.com/user-attachments/assets/254621de-de35-4ccb-b1f6-88d708a9554a" />
**Total Spent time: 02:03:26**
<img width="797" height="584" alt="Снимок экрана 2026-10-02 224113" src="https://github.com/user-attachments/assets/df799c4c-a7a8-4dcd-9b84-460f60bc2828" />

# INFORMATION!
After all of this I spent this project to forge moderators. They returned this project and in this moment I came up with the idea of ​​making a custom keycap.
So I just spent more time to do just keycap.

# September 30: Doing Custom Keycaps
I open case project and near the case I started do keycaps. I chose black white gamma style so I don't use and other colors. Somethink hard I didn't do just added in every keycap text like home,  1,  f8, and in big keycaps like spacebar I just opened edit mode and edit keycaps.
**Total Spent time: 3:05:06**
<img width="1065" height="337" alt="Снимок экрана 2026-10-02 224205" src="https://github.com/user-attachments/assets/5074ef5f-b144-4697-95d9-f14078a6e8ff" />
# TOTAL TIME OF ALL DAYS: 9:42:21 (9 hours 42 minutes 21 secons)


**OBS https://youtu.be/j6rzwQuYg7c**
**Timelaps https://youtu.be/f1GuJOrHSng**
