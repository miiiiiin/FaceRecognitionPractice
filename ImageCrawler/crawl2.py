import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = '/Users/songkyungmin/Downloads/chromedriver'
query = '뉴진스 민지'

driver = webdriver.Chrome()
driver.get(f'https://https://www.google.com/imghp')

# search
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys(query)
search_bar.submit()

PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
new_height = 0
while True:
    driver.execute_script("window.scrollBy(0, 5000")
    time.sleep(PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height - last_height > 0:
        last_height = new_height
        continue
    else:
        break

# 확인한 프로퍼티로 클릭할 image element list 얻기
img_elements = driver.find_element(By.CSS_SELECTOR, ".rg_i")

# 해당 이미지들 클릭하여 필요한 정보 획득
img_rst = []

for idx, img in enumerate(img_elements) :
    print(f"{query} : {idx+1}/{len(img_elements)} proceed...")

try :

    img.click()

    time.sleep(PAUSE_TIME)

    img_element = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')

    img_src = img_element.get_attribute('src')

    img_alt = img_element.get_attribute('alt')

    img_rst.append({

        'alt' : img_alt,
        'src' : img_src

    })

except :
    pass

driver.close()