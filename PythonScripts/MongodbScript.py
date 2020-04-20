from bs4 import BeautifulSoup
from requests import get
import re
from ConnectToDatabase import *

itemsToInsert = []
items = ["White Raffard's Decoction","Swallow","White Honey","Ekhidna decoction","Troll decoction" ,"Ekimmara decoction","Grave hag decoction",
         "Thunderbolt","Petri's Philter","Black Blood","Tawny Owl", "Maribor Forest", "Leshen decoction", "Nekker warrior decoction",
         "Katakan decoction", "Ancient leshen decoction", "Alghoul decoction", "Basilisk decoction", "Chort decoction",
         "Doppler decoction", "Foglet decoction", "Forktail decocion", "Succubus decoction", "Water hag decoction",
         "Wyvern decoction", "Full Moon", "Golden Oriole", "Blizzard", "Griffin decoction", "Reliever's decoction",
         "Earth elemental decoction", "Arachas decoction", "Nightwraith decoction", "Noonwraith decoction", "Cat_(potion)",
         "Fiend decoction", "Cockatrice decoction", "Werewolf decoction", "Killer whale"]


enemiesToInsert = []
enemies = ["Ghoul", "Dog", "Drowner", "Nekker", "Wraith", "Water hag", "Griffin_(creature)", "Noonwraith", "nightwraith"]
enemiesRecognised = ["Ghoul", "Dog", "Drowner", "Nekker", "Wraith", "Water hag", "Griffin"]
tactics = ""


class Enemy:
  def __init__(self, tempName,tempLongTactic, tempShortTactic):
     self.name = tempName
     self.longCombatTactics = tempLongTactic
     self.shortCombatTactics = tempShortTactic

class Alchemy:
    def __init__(self, tempName, tempEffect, tempIngredient):
        self.name = tempName
        self.effect = tempEffect
        self.ingredients = tempIngredient




def insertEnemies():
    collection = db.Enemies
    for x in enemies:
        url = 'https://witcher.fandom.com/wiki/' + x
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)

        tactics = ""
    #    print("name: " + html_soup.find("h1").text)

        tempName = html_soup.find("h1").text

        combatTactics = html_soup.find(id ="Combat_tactics").parent
        combatTacticsp = combatTactics.nextSibling

        for n in range(20):
            combatTacticsp = combatTacticsp.next_element
            p = str(combatTacticsp)

            if p.__contains__('<p'):
                tactics += p
            if p.__contains__('<h') or n == 20:
                break
        tactics += "\n \n"
       # print("longTactic: " + re.sub('<.*?>', '', tactics.strip()))

        tempLongTactic = re.sub('<.*?>', '', tactics.strip())

        index = 0
        combatTactics = html_soup.find_all("h3", class_="pi-data-label pi-secondary-font")[index]
        found = False

        while found is False:
                if combatTactics.text != "Susceptibility":
                    index = index + 1
                    combatTactics = html_soup.find_all("h3", class_="pi-data-label pi-secondary-font")[index]
                else:
                    found = True

        rawdata = str(combatTactics.nextSibling.nextSibling)

        finalText = re.sub('<.*?>', ' ', rawdata)
        finalText = re.sub(' +', ' ', finalText)

       #print("ShortTactic: " + finalText.strip())
        tempShortTactic = finalText.strip()
        tempEnemy = Enemy(tempName,tempLongTactic , tempShortTactic)
        enemiesToInsert.append(tempEnemy)



    for e in enemiesToInsert:
           # print(e.name)
            test = {
                    "name":e.name.lower(),
                    "longCombatTactic": e.longCombatTactics.lower(),
                    "shortCombatTactic": e.shortCombatTactics.lower()
                    }
            collection.insert_one(test)



def insertAlchemy():
    print("INSERT")
    collection = db.Alchemy

    for item in items:
        url = 'https://witcher.fandom.com/wiki/' + item
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)
        index = 0
        skip = False
        tempName = ""
        tempEffect = ""
        tempIngredient = []

        if html_soup.find(id="The_Witcher_3:_Wild_Hunt") is None:
            Ingredients = html_soup.find("h2", class_="pi-item pi-item-spacing pi-title")
            if str(Ingredients) == "None":
                continue
            # name
            #print(html_soup.find("h1").text)
            tempName = html_soup.find("h1").text.strip()
            Ingredients = html_soup.find("h2",
                                         class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
            Ingredients = Ingredients.findNext("h2",
                                               class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
            Ingredients = Ingredients.findNext("h2",
                                               class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
            info = Ingredients
            Ingredients = Ingredients.findNext("h3").findNext("div")
            # Effect
            #print(Ingredients.text)
            tempEffect = Ingredients.text.strip()

            info = Ingredients.findNext("h2",
                                        class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
            Ingredients = info.findNext("h3").findNext("h3").findNext("div")
            finalText = re.sub('<.*?>', ' ', str(Ingredients))
            finalText = re.sub(' +', ' ', finalText)
            # Ingredients needed
            # print(finalText)

            test = ""
            counter = 0
            for char in finalText.strip():
                if char.isdigit() and counter == 1:
                    char = ", " + char
                test = test + char
                counter = 1
            #ingredients needed with seperator
            #print(test)
            tempIngredient = test.split(",")
        else:
            skip = True

        if skip is True:
            # name
            #print(html_soup.find("h1").text)
            tempName = str(html_soup.find("h1").text)

            Ingredients = html_soup.find(id="The_Witcher_3:_Wild_Hunt").parent
            Ingredients = Ingredients.findNext("h2",
                                               class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")

            info = Ingredients
            text = ""
            while text != "Attributes":
                Ingredients = Ingredients.findNext("h2",
                                                   class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
                text = Ingredients.text

            Ingredients = Ingredients.findNext("h3")
            text = Ingredients.text
            while text != "Effect(s)":
                Ingredients = Ingredients.findNext("h3")
                text = Ingredients.text

            rawdata = str(Ingredients.nextSibling.nextSibling)
            finalText = re.sub('<.*?>', ' ', rawdata)
            finalText = re.sub(' +', ' ', finalText)
            # effects
            #print(finalText)
            tempEffect = finalText

            ###

            Ingredients = info
            while text != "Alchemy":
                Ingredients = Ingredients.findNext("h2",
                                                   class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
                text = Ingredients.text

            Ingredients = Ingredients.findNext("h3")
            text = Ingredients.text
            while text != "Ingredients":
                Ingredients = Ingredients.findNext("h3")
                text = Ingredients.text

            rawdata = str(Ingredients.nextSibling.nextSibling)
            finalText = re.sub('<.*?>', ' ', rawdata)
            finalText = re.sub(' +', ' ', finalText)
            # ingredients needed
            #print(finalText)

            test = ""
            counter = 0
            for char in finalText.strip():
                if char.isdigit() and counter == 1:
                    char = ", " + char
                test = test + char
                counter = 1
            tempIngredient = test.split(",")

        tempAlchemy = Alchemy(tempName, tempEffect, tempIngredient)
        itemsToInsert.append(tempAlchemy)



    for i in itemsToInsert:
            test = {
                    "name":i.name.lower(),
                    "effect": i.effect.lower(),
                    "ingredients": i.ingredients
                    }
            collection.insert_one(test)
