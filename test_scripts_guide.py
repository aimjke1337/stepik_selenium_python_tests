from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")

# Метод execute_script() позволяет выполнить программу, написанную на языке JavaScript, как часть сценария автотеста в запущенном браузере
# Метод scrollIntoView позволяет проскроллить страницу до нужного элемента чтобы он был полностью в поле зрения, если элемент например перекрыт чем то другим
# Также можно использовать метод button.location_once_scrolled_into_view или можно использовать метод .submit() вместо .click(), в этом случае кнопка нажмется даже если она скрыта

browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)