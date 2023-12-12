from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Thêm tùy chọn để vô hiệu hóa cảnh báo bảo mật
chrome_options.add_argument('--disable-extensions')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')

import pickle
import os

with open("urls.data", "rb") as file:
    data = pickle.load(file)

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

cnt = 0

for row in data:
    if len(row) == 0:
        continue
    else:

        driver = webdriver.Chrome(options=chrome_options)  # Or the appropriate driver for your browser

        folder_path = f'screenshots/{cnt}'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for index, url in enumerate(row):

            try:
                driver.get(url)
                driver.save_screenshot(f'screenshots/{cnt}/screenshot_{index}.png')
            except:
                print('err') 

        driver.quit()
        cnt += 1
