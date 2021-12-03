from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import unittest
import time
import pyautogui

url="https://boinfbxwiq:15301/FrontOffice/Home/Login"
#url="https://boinfii10q07:60211/FrontOffice/Home/Login/?ReturnUrl=%2FFrontOffice"
count=1
class AcuerdosComerciales(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path='./chromedriver')

	def captura_pantalla(self):
		global count
		nombre="evidencia"+str(count)
		evidencia= pyautogui.screenshot()
		evidencia.save("./"+nombre+".png")
		count+=1
	def test_login(self):

		driver=self.driver
		driver.maximize_window()
		driver.get(url)
		
		configuracion_avanzada=driver.find_element_by_id("details-button").click()
		continuar_a=driver.find_element_by_id("proceed-link").click()
	
		usuario=driver.find_element_by_id("IdentificadorCodigo")
		contraseña= driver.find_element_by_id("Clave")
		usuario.send_keys("OOP07199")
		contraseña.send_keys("Patacon22*")
		contraseña.send_keys(Keys.ENTER)
	
		continuar=driver.find_element_by_xpath('//*[@id="chartConfirmacion"]/div[2]/div[1]/button')
		continuar.click()
		self.captura_pantalla()
		


	def crear_acuerdo(self, t_acuerdo):# funcion para crear acuerdos recibe parametro para definir si es estandar "1" o portafolio "2"
		self.test_login()#se reutiliza el caso de login par realizar la creación de un acuerdo comercial
		self.t_acuerdo=t_acuerdo

		#paso 1 selección y cargue del pdf 		
		driver=self.driver
		crear=driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div/div/form/div[6]/div/a')
		crear.click()
	
		tipo_acuerdo=Select(driver.find_element_by_id("TipoAcuerdoComercial"))
		tipo_acuerdo.select_by_value(t_acuerdo)
		
		adjuntar= driver.find_element_by_id("ArchivoAdjunto")
		adjuntar.send_keys('C:\\Users\\OOP07199\\Pictures\\AC_Pruebas_QA.pdf')#sube el archivo pdf indicado en ruta
		
		continuar=driver.find_element_by_id("Continuar").click()

		
		#paso 2 formulario
		tipo_documento=Select(driver.find_element_by_id("TipoDocumento"))
		tipo_documento.select_by_value("3")
		num_documento=driver.find_element_by_id("NumeroDocumento")
		num_documento.send_keys("9001543412 ")#("8902119023")
		if(t_acuerdo=="1"):#valida si es estandar y agrega el saldo promedio si no, continua
			saldo_promedio= driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/form/div[3]/div[1]/div[9]/div/input')
			saldo_promedio.send_keys(Keys.BACKSPACE)
			saldo_promedio.send_keys("333333333")
			tipo_cuenta_aho= driver.find_element_by_xpath("/html/body/div[1]/main/div/div/div/form/div[3]/div[1]/div[10]/div/div[1]/label/input")
			tipo_cuenta_cte=driver.find_element_by_xpath("/html/body/div[1]/main/div/div/div/form/div[3]/div[1]/div[10]/div/div[2]/label/input")
			tipo_cuenta_aho.click()
			tipo_cuenta_cte.click()
		else:
			
			tipo_cuenta_aho=driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/form/div[3]/div[1]/div[9]/div/div[1]/label/input')
			tipo_cuenta_cte=driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/form/div[3]/div[1]/div[9]/div/div[2]/label/input')
			tipo_cuenta_aho.click()
			tipo_cuenta_cte.click()

		
		continuar_paso2=driver.find_element_by_id("Continuar")
		continuar_paso2.click()
		# paso 3 plan pareja
		
		time.sleep(3)
		plan_pareja=driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[2]/td[1]/input')
		plan_pareja.click()
		
		self.captura_pantalla()
		continuar_paso2=driver.find_element_by_id("Continuar")
		continuar_paso2.click()

		#paso 3
		producto=Select(driver.find_element_by_id("TarifaPlena"))
		producto.select_by_index(24)
		cantidatrasacciones=driver.find_element_by_id("CantidadTransacciones")
		cantidatrasacciones.send_keys("3")
		tarifaespecialsinIVA= driver.find_element_by_id("TarifaEspecialSinIva")
		tarifaespecialsinIVA.send_keys("999")
		seleccionarcuentas=driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div/div/form/div[3]/div[1]/div[5]/div/button[1]")
		seleccionarcuentas.click()
		time.sleep(5)
		self.captura_pantalla()



	def test_crea_acuerdo_comercial_portafolio(self):
		self.crear_acuerdo("2")

	def crea_acuerdo_comercial_estandar(self):
		self.crear_acuerdo("1")	



	def tearDown(self):
		self.driver.close()

		

if __name__ == '__main__':
    unittest.main()

