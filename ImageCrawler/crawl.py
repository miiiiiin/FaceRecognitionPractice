from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

PAUSE_TIME = 2
count = 1

driver = webdriver.Chrome()
driver.get('https://www.google.co.kr/imghp')


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def crawling_images(query):
    createDirectory(f'train_dataset/{query}')

    # 쿼리 검색 및 검색 버튼 클릭
    elem = driver.find_element('name', 'q')
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)

    # 이미지 스크롤링
    last_height = driver.execute_script("return document.body.scrollHeight")
    new_height = 0

    while True:
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height - last_height > 0:
            last_height = new_height
            continue
        else:
            break

    # 이미지 수집 및 저장
    images = driver.find_elements(By.CSS_SELECTOR, ".mNsIhb")  # 각 이미지들의 class
    count = 1
    print("imgs check:", len(images))
    for image in images:
        try:
            image.click()
            # print("img: ", image.get_attribute("class"))
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,
                                         '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img').get_attribute(
                "src")

            print("imageurl:", imgUrl)
            imgUrl = imgUrl.replace('https', 'http')  # https로 요청할 경우 보안 문제로 SSL에러가 남
            opener = urllib.request.build_opener()
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0')]  # https://docs.python.org/3/library/urllib.request.html 참고
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, f'train_dataset/{query}/{query}_{str(count)}.jpg')
            count = count + 1
            print(f'--{count}번째 이미지 저장 완료--')

        except Exception as e:
            print('Error : ', e)
            pass

    driver.close()


# def crawling_img(query):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = '/Users/songkyungmin/Downloads/chromedriver'
#
#     driver = webdriver.Chrome()
#     driver.get(f'https://www.google.com/imghp')
#     search_bar = driver.find_element(By.NAME, "q")
#     search_bar.send_keys(query)
#     search_bar.submit()
#
#     PAUSE_TIME = 2
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     new_height = 0
#
#     while True:
#         driver.execute_script("window.scrollBy(0,5000)")
#         time.sleep(PAUSE_TIME)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#
#         if new_height - last_height > 0:
#             last_height = new_height
#             continue
#         else:
#             break
#
#     img_elements = driver.find_elements(By.CSS_SELECTOR, ".mNsIhb")
#     imgs = []
#
#     print("elements: ", len(img_elements))
#
#     PAUSE_TIME = 2
#     last_hegiht = driver.execute_script("return document.body.scrollHeight")
#     new_height = 0
#
#     while True:
#         driver.execute_script("window.scrollBy(0,1000)")
#         time.sleep(PAUSE_TIME)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#
#         if new_height - last_hegiht > 0:
#             last_hegiht = new_height
#             continue
#         else:
#             break
#
#     for idx, img in enumerate(img_elements):
#         print(f"{query} : {idx + 1}/{len(img_elements)} proceed...")
#         print("image downloading")
#
#         try:
#             img.click()
#             time.sleep(PAUSE_TIME)
#             # 이부분에서 에러나면, 직접 개발자 도구 활용해서 XPATH 추출한 뒤에 변경
#             # img_element = driver.find_element(By.XPATH, '//img[@class="//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[2]')
#             # img_element = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]')
#             # img_src = img_element.get_attribute('src')
#             # print("src:", img_src)
#             #
#             # img_alt = img_element.get_attribute('alt')
#             # imgs.append({
#             #     'alt': img_alt,
#             #     'src': img_src
#             # })
#

#########################################################################################
#             imgUrl = driver.find_element(By.XPATH,
#                                          '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img').get_attribute(
#                 "src")
#             print("imageurl:", imgUrl)
#             imgUrl = imgUrl.replace('https', 'http')  # https로 요청할 경우 보안 문제로 SSL에러가 남
#             opener = urllib.request.build_opener()
#             print("opener:", opener)
#             opener.addheaders = [
#                 ('User-Agent', 'Mozilla/5.0')]  # https://docs.python.org/3/library/urllib.request.html 참고
#             urllib.request.install_opener(opener)
#
#         except Exception as e:
#             print(f'err in {idx}, {e}')
#             pass
#
#     save_path = f'/Users/songkyungmin/Downloads/imgData/{query}'
#     if not os.path.exists(save_path):
#         os.mkdir(save_path)
#
#     total_N = len(imgs)
#     for idx, one in enumerate(imgs):
#         src = one['src']
#         alt = one['alt']
#         urllib.request.urlretrieve(src, f"{save_path}/{query}_{idx}.png")
#         print(idx, alt)
#
#     print('done')
#     driver.close()


names = ["노홍철"]
# names = ["뉴진스 하니"]
for name in names:
    crawling_images(name)

