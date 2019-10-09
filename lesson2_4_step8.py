#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#Нажать на кнопку "Book"
#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math
from math import log
from math import sin

def calc(x):
  return log(abs(12*sin(x)))
  
  
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #ждем пока цена не будет 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
        )
    
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
        )
    
    button.click()    

    # Считываем значение переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    #alert(x)
    
    f = calc(int(x))

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(str(f))
    
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()  

      

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()