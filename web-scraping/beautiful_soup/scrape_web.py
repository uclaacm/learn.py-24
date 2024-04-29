import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"
page = requests.get(URL)
htmlData = page.content

soup = BeautifulSoup(htmlData, "html.parser")
print(soup.prettify())

with open("parsed_output.html", 'w', encoding='utf-8') as file:
    file.write(soup.prettify())