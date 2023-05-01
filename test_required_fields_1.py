from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CLASS_NAME, "first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CLASS_NAME, "second")
    last_name.send_keys("Konnov")

    email = browser.find_element(By.CLASS_NAME, "third") 
    email.send_keys("test@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    print("Успешно")
    time.sleep(10)
    browser.quit()    