from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()

# Thêm tùy chọn để vô hiệu hóa cảnh báo bảo mật
chrome_options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome(options=chrome_options)
driver.get("C:\\Users\\votru\\Desktop\\phish\\screenshots\\0\\screenshot_19.html")

time.sleep(10)