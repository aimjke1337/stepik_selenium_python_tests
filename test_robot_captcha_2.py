from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    # Подключение драйвера и переход по ссылке
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим картинку и забираем у нее значение аттрибута и подставляем это значение в функцию
    findX = browser.find_element(By.ID, 'treasure')
    getX = findX.get_attribute("valuex")
    print("value of treasure: ", getX)
    x = getX
    y = calc(x)

    # Находим поле для ответа и вставляем туда значение полученное из функции
    answer_area = browser.find_element(By.CSS_SELECTOR, '#answer, required')
    answer_area.send_keys(y)
    
    # Находим чекбокс и проставляет галочку
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    # Находим радиобаттон и переключаем на нужное значение
    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()
    
    # Находим кнопку подтвердить и нажимаем ее
    btn_submit = browser.find_element(By.CSS_SELECTOR, 'button, [type="submit"]')
    btn_submit.click()

finally:
    # Ждем 4 секунды и закрываем браузер
    time.sleep(4)
    browser.quit()  