from selenium import webdriver
URL = 'https://rahulshettyacademy.com/AutomationPractice'
driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://rahulshettyacademy.com/")
driver.minimize_window()
#print(driver.title)
#print(driver.current_url)
driver.get(URL)
driver.back()
driver.refresh()
driver.close()
