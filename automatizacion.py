# Import selenium module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
  
  
# Using chrome driver
driver = webdriver.Chrome('c:/chromedriver')
  
  
# Web page url
driver.get("https://google.com")
  
driver.quit()