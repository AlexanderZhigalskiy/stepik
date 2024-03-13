from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element(By.ID, "book").click()


x_element = browser.find_element(By.CSS_SELECTOR, "[id = 'input_value']")
x = x_element.text
y = calc(x)

button = browser.find_element(By.CSS_SELECTOR,"[name='text']")
button.send_keys(y)

enter = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
enter.click()

time.sleep(5)

