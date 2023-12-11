from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Chrome()
driver.get('http://www.naver.com')
element=driver.find_element(By.ID,'query')
element.send_keys(Keys.RETURN)
driver.find_element(By.ID,'gnb_login_button').click()

uid='nave'
upw='vaerrr3231313'

input_js ='document.getElementById("id").value="{id}";document.getElementById("pw").value="{pw}";'.format(id=uid,pw=upw)
#js코드로 

time.sleep(1)
driver.excute_script(input_js)
time.sleep(1)
driver.find_element(By.ID,"log.login").click()
time.sleep(1)
os.system("pause")