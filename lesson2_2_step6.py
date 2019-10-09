#Открыть страницу http://SunInJuly.github.io/execute_script.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x.
#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Выбрать checkbox "I'm the robot".
#Переключить radiobutton "Robots rule!".
#Нажать на кнопку "Submit".

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
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    f = calc(int(x))

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(str(f))

    #прокрутим браузер немного ниже
    browser.execute_script("window.scrollBy(0, 100);")


    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click()
    
    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()

    #прокручиваем форму до кнопки чтобы ее нажать
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()