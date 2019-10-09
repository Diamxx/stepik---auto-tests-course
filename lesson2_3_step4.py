#Открыть страницу http://suninjuly.github.io/alert_accept.html
#Нажать на кнопку
#Принять confirm
#На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
from math import log
from math import sin

def calc(x):
  return log(abs(12*sin(x)))
  
  
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #прокручиваем форму до кнопки чтобы ее нажать
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()    

    confirm = browser.switch_to.alert
    confirm.accept()

    # Считываем значение переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    f = calc(int(x))

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(str(f))
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()  

      

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()