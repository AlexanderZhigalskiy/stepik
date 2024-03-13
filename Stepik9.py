from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

submit = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
submit.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.CSS_SELECTOR, "[id = 'input_value']")
x = x_element.text
y = calc(x)

button = browser.find_element(By.CSS_SELECTOR,"[name='text']")
button.send_keys(y)

enter = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
enter.click()

time.sleep(5)
