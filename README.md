# Morse Code Input

As part of the 2016 [#includeathon](http://hackathon.includegirls.com)
challenge, Isaac Ortiz and Humberto Ortiz-Zuazaga decided to attempt
the challenge: Control the keyboard and mouse vía Morse Code.

## Morse Code 

![Morse code chart](International_Morse_Code.svg)

By Rhey T. Snodgrass & Victor F. Camp, 1922 - Image:Intcode.png and
Image:International Morse Code.PNG, Public Domain,
https://commons.wikimedia.org/w/index.php?curid=3902977

http://morsecode.scphillips.com/morse.html

##  Input options

#. left click is dot, right click is dash.
#. short press is dot, long press is dash.

We've only implemented #1.

## Prerequisites

Morseshim is written in python3.

The requirements.txt files lists the python modules we use, autogui
and pynput. You can try installing from the requirements file, but on
Ubuntu I had to install a few extra packages. See the instalation
instructions for autogui on their page:

<https://pyautogui.readthedocs.io/en/latest/>

The pynput module allows reading and writing keyboard and mouse events
as well. It may be possible to make this program with only pyinput. I
leave the exercise to the reader.

## Running

To run the program run python3 morseshim.py in a terminal.

The program will listen to left and right clicks, and translate them
to dots and dashes. To end a letter, long press the last morse
character of the letter. For example, H is di di di dit in morse
(....), so you should do:

Left click
Left click
Left click
Press and hold left, then release.

The program doesn't have to have the input focus to receive events, so
you can use it to control any program.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
