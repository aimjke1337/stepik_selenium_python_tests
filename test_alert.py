from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    press_btn = browser.find_element(By.CSS_SELECTOR, ".container > .btn ").click()

    modal = browser.switch_to.alert
    modal.accept()

    # Находим значение X и вызываем функцию подсчета значения примера
    getX = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value')
    x = getX.text
    y = calc(x)

    # Находим поле для ответа и вставляем туда значение полученное из функции
    answer_area = browser.find_element(By.CSS_SELECTOR, '#answer, required')
    answer_area.send_keys(y)

    # Находим кнопку подтвердить и нажимаем ее
    btn_submit = browser.find_element(By.CSS_SELECTOR, 'button, [type="submit"]')
    btn_submit.click()

finally:
    time.sleep(10)
    browser.quit()    



# метод switch_to. дает возможность переключиться на модальное окно в пример "alert"

#alert = browser.switch_to.alert
#alert.accept()   - принять 
#alert.dissmiss() - Отмена
#promt.send_keys("answer")
#promt.accept()

#alert = browser.switch_to.alert
#alert_text = alert.text