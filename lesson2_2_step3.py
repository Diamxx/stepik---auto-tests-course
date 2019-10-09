from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x,y):
  return x+y
  
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение переменной х
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    
    
    # Считываем значение переменной y
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    
    
    sum = calc(int(x),int(y))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum)) # ищем сумму в выпадающем списке

  
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()