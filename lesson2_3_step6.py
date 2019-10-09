#Открыть страницу http://suninjuly.github.io/redirect_accept.html
#Нажать на кнопку
#Переключиться на новую вкладку
#Пройти капчу для робота и получить число-ответ

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
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1) 
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()    

    windows = browser.window_handles
    current_window = browser.current_window_handle

    index=0
    for win in windows:
        if current_window == win:
            index = windows.index(win)+1
            break
    
    new_window = browser.window_handles[index]
    browser.switch_to.window(new_window)


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