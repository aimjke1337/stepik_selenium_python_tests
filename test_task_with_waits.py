from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    wait_price = WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_btn = browser.find_element(By.ID, "book")
    book_btn.click()

    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    y = calc(x)

    answer_area = browser.find_element(By.ID, "answer")
    answer_area.send_keys(y)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
   

