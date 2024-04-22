# research

## choosing a library
beautiful soup is for simpler static websites whereas selenium is more powerful, for dynamic websites
we need selenium for ny times

make sure python is installed

## selenium installation and first script
https://www.selenium.dev/documentation/webdriver/getting_started/install_library/

## progress

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://downforacross.com/beta/game/5104299-plusk")

driver.implicitly_wait(2)

# enter list view
listview_button = driver.find_element(by=By.CLASS_NAME, value="toolbar--list-view")
listview_button.click()

driver.implicitly_wait(.5)


clues = driver.find_elements(by=By.CLASS_NAME, value="list-view--list--clue")

for clue in clues:
    clue_num = clue.find_element(by=By.CLASS_NAME, value="list-view--list--clue--number")
    print(clue_num.text)

driver.quit()
```

explicit waits are important (e.g. to wait for model to appear)