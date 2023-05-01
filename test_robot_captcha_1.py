from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"



try:
    # Подключение драйвера и переход по ссылке
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение X и вызываем функцию подсчета значения примера
    getX = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value')
    x = getX.text
    y = calc(x)


    # Проверка что у радиобаттона есть атрибут checked
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")

    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"


    # Находим поле для ответа и вставляем туда значение полученное из функции
    answer_area = browser.find_element(By.CSS_SELECTOR, '#answer, required')
    answer_area.send_keys(y)
    
    # Находим чекбокс и проставляет галочку
    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()

    # Находим радиобаттон и переключаем на нужное значение
    radio_button = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    radio_button.click()
    
    # Находим кнопку подтвердить и нажимаем ее
    btn_submit = browser.find_element(By.CSS_SELECTOR, 'button, [type="submit"]')
    btn_submit.click()

finally:
    # Ждем 4 секунды и закрываем браузер
    time.sleep(4)
    browser.quit()   

   