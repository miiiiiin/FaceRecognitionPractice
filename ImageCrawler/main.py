from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("뉴진스 민지")
elem.send_keys(Keys.RETURN)

# 스크롤 내리기
SCROLL_PAUSE_TIME = 1

# GET SCROLL HEIGHT
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 아래 끝까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 페이지 로드될 때까지 기다리기
    time.sleep(SCROLL_PAUSE_TIME)

    # 지난 스크롤 높이와 비교하여 새 스크롤 높이 계산
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break

    last_height = new_height

# 스크롤 끝
images = driver.find_element_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(3)
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.close()

# @staticmethod
# def get_keywords(keywords_file='keywords.txt'):
#     with open(keywords_file, 'r', encoding='utf-8-sig') as f:
#         text = f.read()
#         lines = text.split('\n')
#         lines = filter(lambda x: x != '' and x is not None, lines)
#         keywords = sorted(set(lines))
#
#     print('{} keywords found: {}'.format(len(keywords), keywords))
#
#     # re-save sorted keywords
#     with open(keywords_file, 'w+', encoding='utf-8') as f:
#         for keyword in keywords:
#             f.write('{}\n'.format(keyword))
#
#     return keywords