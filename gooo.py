import keyboard as kb
from pynput import keyboard
import time
import easygui as es
es.msgbox(msg="Listo para Iniciar", title="Robot", ok_button="Iniciar", root='Top')
time.sleep(5)
def finaliza():
    exit()

# It writes the keys r, k and endofline
kb.press_and_release('tab')
time.sleep(0.1)
kb.write("1069745629")
kb.press_and_release('Enter')
time.sleep(0.1)
es.msgbox(msg="Finalizado", title="Robot", ok_button="Salir", root='Top')
"""for a in range(25):
    kb.press_and_release('Up')
    time.sleep(0.5)
# it blocks until ctrl is pressed"""
hotkeys = {'<shift>+q': finaliza}

#escuchador con la clase GlobalHotKeys
with keyboard.GlobalHotKeys(hotkeys) as l:
    l.join()

