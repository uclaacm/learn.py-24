from bs4 import BeautifulSoup

with open("frieren_fanpage.html", 'r', encoding="utf-8") as file:
    html = file.read() # Read the entire content of the file into a string

# Create a BeautifulSoup object by parsing the HTML content
soup = BeautifulSoup(html, "html.parser")

#_______________________________________________________________________________

# Extract all the text from the page
text = soup.get_text()
print(text)

#_______________________________________________________________________________

# Find elements by HTML class name
title_element = soup.find("h1") # Find all the first <h1> tag in the document
print(title_element)
print(title_element.text) # We can use the .text attribute to extract clean, human-readable text without any HTML tags

character_elements = soup.find_all("li") # Find all <li> tags in the document
for character_element in character_elements:
    print(character_element.text)

# There are 4 <li> tags in total, but this code only finds the first two
soup.find_all("li", limit=2)

#_______________________________________________________________________________

# Find elements by CSS class name and id
styled_elements = soup.find_all(class_="some_styling")
for styled_element in styled_elements:
    print(styled_element)

link_element = soup.find(id="official_link")
print(link_element)

#_______________________________________________________________________________

# Find elements by text content
description_heading = soup.find("h2", string="Description") # Find the <h2> tag that contains the exact text 'Description'

#_______________________________________________________________________________

# Navigation methods
description_element = description_heading.find_next_sibling("p") # # Find the next <p> tag immediately following the <h2> tag
print(description_element.text)

description_element_2 = description_heading.find_next("p")
print(description_element_2.text)
