# reveal answers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# selenium setup
driver = webdriver.Chrome()
driver.get("https://downforacross.com/?search=ny+time")
wait = WebDriverWait(driver, timeout=20)

# get all entries
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "entry--container")))
entry_containers = driver.find_elements(by=By.CLASS_NAME, value="entry--container")

# iterate over entry--container divs
for i in range(len(entry_containers)):
    # need to get again because the page reloads
    entry = driver.find_elements(by=By.CLASS_NAME, value="entry--container")[i]

    # click on a tag in entry
    entry.find_element(by=By.TAG_NAME, value="a").click()

    # wait for page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "toolbar--list-view")))

    # enter list view
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "toolbar--list-view")))
    listview_button = driver.find_element(by=By.CLASS_NAME, value="toolbar--list-view")
    listview_button.click()

    ##############################
    # NEW: reveal answers ########
    reveal_div = driver.find_element(by=By.CLASS_NAME, value="reveal")
    reveal_div.find_element(by=By.CSS_SELECTOR, value="button").click()

    reveal_puzzle = reveal_div.find_elements(by=By.CLASS_NAME, value="action-menu--list--action")[2]
    reveal_puzzle.click()

    confirm_button = driver.find_element(by=By.CLASS_NAME, value="swal-button--danger")

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--danger")))
    confirm_button.click()
    ##############################

    # go back to ny times results page
    driver.back()

    # wait for page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "entry--container")))

driver.quit()