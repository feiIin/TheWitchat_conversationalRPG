from bs4 import BeautifulSoup
from requests import get
import re

# DEPRECATED CODE!!!
# THIS IS THE WAY TO SCRAPE THE DATA OF THE SHORT COMBAT TACTICS OF THE ENEMIES FROM THE WIKI.
# IF YOU WANT TO SCRAPE THE DATA FROM THE WIKI TO FILL THE DATABASE PLEASE REFER TO THE MONGODBSCRIPT FUNCTIONS

enemies = ["Ghoul", "Dog", "Drowner", "Nekker", "Wraith", "Water hag", "Griffin_(creature)", "Noonwraith", "nightwraith"]
tactics = ""
for x in enemies:
    url = 'https://witcher.fandom.com/wiki/' + x
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    index = 0
    combatTactics = html_soup.find_all("h3", class_="pi-data-label pi-secondary-font")[index]
    found = False
    while found == False:
        if combatTactics.text != "Susceptibility":
            index = index + 1
            combatTactics = html_soup.find_all("h3", class_="pi-data-label pi-secondary-font")[index]
        else:
            found = True
    rawdata = str(combatTactics.nextSibling.nextSibling)

    finalText = re.sub('<.*?>', ' ', rawdata)
    finalText = re.sub(' +', ' ',finalText)

    print(finalText)

