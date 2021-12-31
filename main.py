from pynput import keyboard
import voiceInterpreter
import window
from time import sleep

def on_release(key):
    try:
        print('Key released: {0}'.format(key))
        if key == keyboard.Key.esc:
            return False
        elif key.char == '\\':
            voiceInterpreter.toggleActive()
    except:
        a = 1

if __name__ == '__main__':\

    mainWindow = window.Window()
