from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение переменной х
    x_treasure = browser.find_element_by_id("treasure")
    x = x_treasure.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("input#robotcheckbox")
    option1.click()

    checkbox1 = browser.find_element_by_css_selector("input#robotsrule")
    checkbox1.click()
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()