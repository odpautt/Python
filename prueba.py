# optine el ancho y alto de la pantalla del PC
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(ancho, alto)