
import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'http://www.naver.com'
driver.get(url)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
elem = driver.find_element(By.XPATH, '//*[@id="query"]')

elem.clear()

elem.send_keys("날씨")
elem.send_keys(Keys.RETURN)
time.sleep(5)

temperature= driver.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/strong').text


driver.close()
print(temperature)

import pandas as pd

