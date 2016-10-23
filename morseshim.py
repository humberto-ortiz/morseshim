# morseshim.py - Listen for morse code and convert to keyboard input
# Copyright 2016 - Humberto Ortiz-Zuazaga and Isaac Ortiz-Pena

#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see
#    <http://www.gnu.org/licenses/>.

import pyautogui, time

# http://pythonhosted.org/pynput/mouse.html

from pynput.mouse import Listener, Button

msg = ""


morse = { "a" : ".-",
          "b" : "-...",
          "c" : "-.-.",
          "d" : "-..",
          "e" : ".",
          "f" : "..-.",
          "g" : "--.",
          "h" : "....",
          "i" : "..",
          "j" : ".---",
          "k" : "-.-",
          "l" : ".-..",
          "m" : "--",
          "n" : "-.",
          "o" : "---",
          "p" : ".--.",
          "q" : "--.-",
          "r" : ".-.",
          "s" : "...",
          "t" : "-",
          "u" : "..-",
          "v" : "...-",
          "w" : ".--",
          "x" : "-..-",
          "y" : "-.--",
          "z" : "--..",
          "1" : ".----",
          "2" : "..---",
          "3" : "...--",
          "4" : "....-",
          "5" : ".....",
          "6" : "-....",
          "7" : "--...",
          "8" : "---..",
          "9" : "----.",
          "0" : "-----"
}

esrom = {v: k for k, v in morse.items() }

lasttime = time.time()

def on_click(x, y, button, pressed):
    global msg
    global lasttime
    
    if pressed:
        if Button.left == button:
            msg += "."
            lasttime = time.time()
        if Button.right == button:
            msg += "-"
            lasttime = time.time()
            
    else:
#        print(msg)
        newtime = time.time()
        #print (newtime - lasttime)
        if (newtime - lasttime) > 0.5:
            print(msg)
            if msg in esrom:

                pyautogui.typewrite(esrom[msg])

            msg = ""
            
    return True

# Collect events forever
with Listener(on_click=on_click) as listener:
    listener.join()
    
