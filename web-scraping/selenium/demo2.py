# building off demo1, enter the password "12345!" into the password field and click submit

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.implicitly_wait(0.5)

password_box = driver.find_element(by=By.NAME, value="my-password")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

password_box.send_keys("12345!_!")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)

driver.quit()