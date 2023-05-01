from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    press_btn = browser.find_element(By.CSS_SELECTOR, ".container > .trollface").click()

    # Задаем переменные вкладкам (название вкладок находим с помощью метода window_handles[index]) и с помощью метода switch_to.window() выбираем на какую вкладку перейти
    new_tab = browser.window_handles[1]
    first_tab = browser.window_handles[0]
    browser.switch_to.window(new_tab)

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


#При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера. WebDriver может работать только с одной вкладкой браузера. 
#При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
#Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:

#browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. 
#Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

#new_window = browser.window_handles[1]
#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

#first_window = browser.window_handles[0]
#После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице