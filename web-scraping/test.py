from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from collections import defaultdict
import json
import time

# selenium setup
driver = webdriver.Chrome()
driver.get("https://downforacross.com/")
wait = WebDriverWait(driver, timeout=5)

# set up database
db = defaultdict(list)

# search for only ny times crosswords
search_bar = driver.find_element(by=By.CLASS_NAME, value="welcome--searchbar")
search_bar.send_keys("ny times")
time.sleep(1.5) # wait for search results to load (might be a better way to do this)

# get all entries
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

    # reveal answers
    reveal_div = driver.find_element(by=By.CLASS_NAME, value="reveal")
    reveal_div.find_element(by=By.CSS_SELECTOR, value="button").click()

    reveal_puzzle = reveal_div.find_elements(by=By.CLASS_NAME, value="action-menu--list--action")[2]
    reveal_puzzle.click()

    confirm_button = driver.find_element(by=By.CLASS_NAME, value="swal-button--danger")

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "swal-button--danger")))
    confirm_button.click()

    # gather clues and answers
    clues = driver.find_elements(by=By.CLASS_NAME, value="list-view--list--clue")

    for clue_div in clues:    
        clue = clue_div.find_element(by=By.CSS_SELECTOR, value="span").text

        # get answer
        grid = clue_div.find_element(by=By.CSS_SELECTOR, value="table")
        cells = grid.find_elements(by=By.CSS_SELECTOR, value="td")
        answer = "".join(cell.find_element(by=By.CLASS_NAME, value="cell--value").text for cell in cells)

        # Add the clue and answer to the database
        for word in clue.split():
            db[word.lower()].append((clue, answer))

    # go back to ny times results page
    driver.back()

    # update JSON file
    with open('/Users/einar/Documents/UCLA/Workshops/learnpy-s24/db.json', 'w') as file:
        json.dump(db, file)

    # wait for page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "entry--container")))

driver.quit()