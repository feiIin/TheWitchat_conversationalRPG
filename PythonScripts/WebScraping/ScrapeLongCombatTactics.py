from bs4 import BeautifulSoup
from requests import get
import re

enemies = ["Ghoul", "Dog", "Drowner", "Nekker", "Wraith", "Water hag", "Griffin_(creature)", "Noonwraith", "nightwraith"]
tactics = ""
for x in enemies:
    url = 'https://witcher.fandom.com/wiki/' + x
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    combatTactics = html_soup.find(id ="Combat_tactics").parent
    combatTacticsp = combatTactics.nextSibling

    for n in range(20):
        combatTacticsp = combatTacticsp.next_element
        p = str(combatTacticsp)
        #print(p[:4].strip())
        if p.__contains__('<p'):
            tactics += p
        if p.__contains__('<h') or n == 20:
            break
    tactics += "\n \n"

finalText = re.sub('<.*?>', '', tactics)
print(finalText)
