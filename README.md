## QMK Linux (Python)

QMK Toolbox is used to flash a compiled .hex file   to a keyboard's PCB. When working with custom keyboards, there is a need to flash the PCB with your desired layout.

This repo is for testing/building for something that could eventually be a working version of QMK Toolbox for Linux.

Credit for QMK Toolbox goes to the great people at <https://qmk.fm/>. See <https://github.com/qmk/qmk_toolbox> for the official QMK Toolbox.


This is NOT an official branch. There is a need for a working version of QMK Toolbox on Linux, and I am trying to find a viable solution.

This is currently written using Python and PyQt5.

You need:

- `pip install requests`
- `pip install pyqt5`

##### What is done:
- GUI complete.

##### To do:
- Detect flash-able USB devices based on vendor (?)
- Flash USB devices using the GUI
- Makefile for install.

