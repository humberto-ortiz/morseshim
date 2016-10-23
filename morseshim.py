#

# Test autogui

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
    
