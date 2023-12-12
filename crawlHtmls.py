from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Thêm tùy chọn để vô hiệu hóa cảnh báo bảo mật
chrome_options.add_argument('--disable-extensions')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')

import pickle
import os
import requests

with open("urls.data", "rb") as file:
    data = pickle.load(file)

if not os.path.exists('htmls'):
    os.makedirs('htmls')

cnt = 0

for row in data:
    if len(row) == 0:
        continue
    else:

        driver = webdriver.Chrome(options=chrome_options)  # Or the appropriate driver for your browser

        folder_path = f'htmls/{cnt}'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for index, url in enumerate(row):

            try:
                response = requests.get(url)

                # Check if the request was successful
                if response.status_code == 200:
                    # Write the content to a file
                    with open(f'htmls/{cnt}/content_{index}.html', 'w', encoding='utf-8') as file:
                        file.write(response.text)
                else:
                    print("Failed to retrieve the webpage")
            except:
                print('err') 

        driver.quit()
        cnt += 1
