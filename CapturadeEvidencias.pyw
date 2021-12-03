import os
from os import listdir

try:
    import easygui as es
except:
    os.system('cmd /k "echo    +--------------------+& echo    + Error libreria Easygui +&echo    +--------------------+&echo .&echo →Se hara upgrade de pip y se instalara Easygui&echo →Cierre para cancelar&echo .&pause&pip install easygui"') 
    os.system('cmd /k "echo    +--------------------+& echo    + Error libreria Pillow +&echo    +--------------------+&echo .&echo →Se hara upgrade de pip y se instalara Easygui&echo →Cierre para cancelar&echo .&pause&pip install pillow"') 


try:
    import pynput
except:
    os.system('cmd /k "echo    +--------------------+& echo    + Error libreria Pynput +&echo    +--------------------+&echo .&echo →Se hara upgrade de pip y se instalara Pynput&echo →Cierre para cancelar&echo .&pause&pip install pynput"') 

from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard
try:
    import pyautogui
except:
    os.system('cmd /k "echo    +--------------------+& echo    + Error libreria Pyautogui +&echo    +--------------------+&echo .&echo →Se hara upgrade de pip y se instalara pyautogui&echo →Cierre para cancelar&echo .&pause&pip install pyautogui"') 
try:
  import cv2
except:
  os.system('cmd /k "echo    +--------------------+& echo    + Error libreria Pynput +&echo    +--------------------+&echo .&echo →Se hara upgrade de pip y se instalara OpenCV&echo →Cierre para cancelar&echo .&pause& pip install opencv-python"') 

 #**********************************************************************************************************************

i = 0
path=""
name=""

def nombre_caso():
  global name
  name=es.enterbox(msg="Digite el número del caso",title="Número de caso")


def mensaje_inicial():
    es.msgbox(msg='                          *** Programa Iniciado ***\n\n\n\nOprima Impr Pant  -->  Captura Evidencia Caso Exitoso\n\nOprima Shift+f  -->  Captura Evidencia Caso Fallido\n\nOprima Esc  -->  Para finalizar el programa\n\n\n\n A contiunuación, seleccione la ruta para guardar las evidencias...',
          title='Toma de Evidencias', 
          ok_button='Continuar')

def mensaje_final():
    es.msgbox(msg='Programa Finalizado',
          title='Toma de Evidencias', 
          ok_button='Finalizar')
    exit()
def captura_dir():# Captura la ruta donde se almacenaran las imagenes
     global path
     path= es.diropenbox(msg="Abrir directorio:",
                           title="Control: diropenbox",
                           default='/home/tcs')

def captura_bug():
  global i
  global path
  global name
  screenshot = pyautogui.screenshot()
  i =i+1
  nombre=name +"_" + str(i)+"_Fallido"
  
  punto_1=(1,1)
  punto_2=(1366,768)
  color=(33,15,255)
  thickness= 10

  screenshot.save(path +"/"+ nombre + ".png")
  img=cv2.imread(path +"/"+ nombre + ".png")
  img=cv2.rectangle(img, punto_1,punto_2, color,thickness)
  cv2.imwrite(path +"/"+ nombre + ".png",img)

def caso_nuevo():
  print("caso nuevo")
  global name, i
  #es.msgbox(msg='Nuevo caso',title='Toma de Evidencias',ok_button='Continuar')
  name=es.enterbox(msg="Digite el número del caso",title="Número de caso")
  i=0

def captura_ok():
  global i
  global path
  global name

  screenshot = pyautogui.screenshot()
  i =i+1
  nombre=name +"_" + str(i)
  punto_1=(1,1)
  punto_2=(1366,768)
  color=(0,215,0)
  thickness= 10

  
  screenshot.save(path +"/"+ nombre + ".png")
  img=cv2.imread(path +"/"+ nombre + ".png")
  img2=cv2.rectangle(img, punto_1,punto_2, color,thickness)
  cv2.imwrite(path +"/"+ nombre + ".png",img)
    

mensaje_inicial()
captura_dir()
if path== None:
  es.msgbox(msg='Ejecución finalizada no se selecciono ruta de almacenamiento',
           title='Toma de Evidencias', 
           ok_button='Salir')
  exit()
nombre_caso()

hotkeys = { '<ESC>': mensaje_final,
'<print_screen>': captura_ok ,
'<shift>+f': captura_bug}

#escuchador con la clase GlobalHotKeys
with keyboard.GlobalHotKeys(hotkeys) as l:
    l.join()
