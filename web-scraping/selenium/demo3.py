# building off demo2, get the text on the confirmation page + modify your code to use explicit waits

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
wait = WebDriverWait(driver, timeout=15)

password_box = driver.find_element(by=By.NAME, value="my-password")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

password_box.send_keys("12345!_!")
submit_button.click()

wait.until(EC.presence_of_element_located((By.ID, "message")))

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)

driver.quit()