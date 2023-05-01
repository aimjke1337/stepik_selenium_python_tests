from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    # Подключение драйвера и переход по ссылке
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим и записываем значение первого числа
    num_1 = browser.find_element(By.ID, "num1")
    num1 = int(num_1.text)

    # Находим и записываем значение второго числа
    num_2 = browser.find_element(By.ID, "num2")
    num2 = int(num_2.text)

    # Складываем полученные числа
    res = num1 +  num2
    

    # Выбираем в выпадающем списке элемент раный нашем значению
    dropdown = Select(browser.find_element(By.TAG_NAME, "select"))
    dropdown.select_by_value(str(res))

    # Находим и нажимаем кнопку подтвердить
    btn_submit = browser.find_element(By.CSS_SELECTOR, 'button, [type="submit"]')
    btn_submit.click()



finally:
    # Ждем 5 секунд и закрываем браузер
    time.sleep(5)
    browser.quit()  