import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = os.environ.get('login')
PASSWORD = os.environ.get('pass')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://tinder.com/')

driver.find_element(By.XPATH, value='//*[@id="u-1919424827"]'
                                    '/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, value='//*[@id="u647161393"]'
                                    '/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()
time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

driver.find_element(By.XPATH, value='//*[@id="email"]').send_keys(LOGIN)
driver.find_element(By.XPATH, value='//*[@id="pass"]').send_keys(PASSWORD)
driver.find_element(By.XPATH, value='//*[@id="loginbutton"]').click()