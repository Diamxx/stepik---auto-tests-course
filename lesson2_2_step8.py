#Открыть страницу http://suninjuly.github.io/file_input.html
#Заполнить текстовые поля: имя, фамилия, email
#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import os

  
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение переменной х
    input_firstname = browser.find_element(By.NAME, "firstname")
    input_firstname.send_keys("Dmitry")

    input_lastname = browser.find_element(By.NAME, "lastname")
    input_lastname.send_keys("K")
    
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("1@1.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.NAME, "file") 
    element.send_keys(file_path)
    
    #прокручиваем форму до кнопки чтобы ее нажать
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()