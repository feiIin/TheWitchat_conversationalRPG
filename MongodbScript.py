from bs4 import BeautifulSoup
from requests import get
import re
from ConnectToDatabase import *

# Initializing arrays. The Items[] and enemies[] are the elements which we are going to scrape data from, from the Website
# The ToInsert arrays are the ones we are going to use to store classes and we are going to push these classes to the database
# The Recognised arrays are the elements which are actually recognised by the Google Speech to Text.
itemsToInsert = []
items = ["White Raffard's Decoction","Swallow","White Honey","Ekhidna decoction","Troll decoction" ,"Ekimmara decoction","Grave hag decoction",
         "Thunderbolt","Petri's Philter","Black Blood","Tawny Owl", "Maribor Forest", "Leshen decoction", "Nekker warrior decoction",
         "Katakan decoction", "Ancient leshen decoction", "Alghoul decoction", "Basilisk decoction", "Chort decoction",
         "Doppler decoction", "Foglet decoction", "Forktail decocion", "Succubus decoction", "Water hag decoction",
         "Wyvern decoction", "Full Moon", "Golden Oriole", "Blizzard", "Griffin decoction", "Reliever's decoction",
         "Earth elemental decoction", "Arachas decoction", "Nightwraith decoction", "Noonwraith decoction", "Cat_(potion)",
         "Fiend decoction", "Cockatrice decoction", "Werewolf decoction", "Killer whale"]

enemiesToInsert = []
enemies = ["Ghoul", "Dog", "Drowner", "Nekker", "Wraith", "Water hag", "Griffin_(creature)", "Noonwraith", "nightwraith" ,"Devil_by_the_Well"]
descriptions = ["Ghouls and graveirs are hard to describe. In part, they resemble humans - yet on the whole, they are the utter negation of all that is human. Though they have arms and legs like men, they walk on all fours like dogs or badgers."
                ," It is fairly common knowledge what a dog is. Generally speaking a dog would not be a target for a witcher. However, there are many cases when dogs become wild, cursed or unnaturally ravenous, sometimes even all of the above."
                ,"Drowners are scoundrels who ended their wicked lives in the water. Drowned alive or thrown into deep water after death, they turn into vengeful creatures which stalk the inhabitants of coastal settlements."
                ,"Nekkers and phoocas live in the dark woods that grow in damp, mist-filled valleys, in colonies of one to several dozen individuals. They dig deep burrows for lairs and connect them with a network of narrow tunnels. Using these passageways they are able to move at great speed within and around their colonies."
                ,"The wraiths are not, as some claim, a projection of an inner fear. They are visible, tangible and dangerous on top of that. The priests teach that people who die suddenly, leaving this vale of tears with important tasks left unfinished, become such ghosts. So wraiths have their own aims. Sometimes they are unaware of them, but more often they aim to achieve them, not caring for the living."
                ,"Water hags, like the drowners and swamp bints with whom they often share hunting grounds, dwell near shallow streams, rivers, and wetlands. Though bulky, they are excellent swimmers. They can even swim through thick mud with astonishing agility, surfacing beside their victims to attack them with their sickle-shaped claws."
                ,"A griffin, also known as griffon or gryphon, is a creature with the body, legs, and tail of a lion and the head, wings, and talons of an eagle. They are known to toy with their prey, eating it alive, piece by piece."
                ,"These monsters appear in fields when the sun is at its highest. Swaying grains on a windless day announce their arrival. They dance in circles in the light of day and draw farmers in to join them. Since they are ghosts, no one who joins them leaves the circle alive."
                ,"Nightwraiths are born of moonlight, wind and the earth cooling after the heat of the day. They rise above the ground and whirl in a mad dance, which should not be seen by any mortal. If caught peeping, the mortal is blinded by moonlight, then taken into the circle and forced to dance until he expires, at times becoming a nightwraith himself."
                ,"Devil by the Well is a unique Noonwraith that is found in the the abandoned village of Hovel, White Orchard."]
enemiesRecognised = ["Ghoul", "Dog", "Drowner", "Nekker", "Wraith", "Water hag", "Griffin"]
tactics = ""


class Enemy:
  def __init__(self, tempName,tempLongTactic, tempShortTactic, tempOccurrence, tempDescription):
     self.name = tempName
     self.longCombatTactics = tempLongTactic
     self.shortCombatTactics = tempShortTactic
     self.occurrence = tempOccurrence
     self.description = tempDescription


class Alchemy:
    def __init__(self, tempName, tempEffect, tempIngredient):
        self.name = tempName
        self.effect = tempEffect
        self.ingredients = tempIngredient


# Running this script allows you to FILL the mongoDb database based on info on the ENEMIES in the witcher 3 WIKI
# NOTE: It only looks for the enemies that are in the array enemies[]
def insertEnemies():
    print("INSERT ENEMIES")
    collection = db.Enemies
    descIndex = 0
    for x in enemies:
        url = 'https://witcher.fandom.com/wiki/' + x
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)

        tactics = ""
    #    print("name: " + html_soup.find("h1").text)

        tempName = html_soup.find("h1").text

        if(html_soup.find(id ="Combat_tactics")):
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

            tempLongTactic = re.sub('<.*?>', '', tactics.strip())
        else:
            tempLongTactic = "Null"

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

        tempShortTactic = finalText.strip()

        index = 0
        combatTactics = html_soup.find_all("h3", class_="pi-data-label pi-secondary-font")[index]
        found = False

        while found is False:
            if combatTactics.text != "Occurrence":
                index = index + 1
                combatTactics = html_soup.find_all("h3", class_="pi-data-label pi-secondary-font")[index]
            else:
                found = True

        rawdata = str(combatTactics.nextSibling.nextSibling)

        finalText = re.sub('<.*?>', ' ', rawdata)
        finalText = re.sub(' +', ' ', finalText)

        tempOccurrence = finalText.strip()

        tempEnemy = Enemy(tempName,tempLongTactic , tempShortTactic, tempOccurrence, descriptions[descIndex])
        enemiesToInsert.append(tempEnemy)
        descIndex = descIndex + 1



    for e in enemiesToInsert:
           # print(e.name)
            test = {
                    "name":e.name.lower(),
                    "longCombatTactic": e.longCombatTactics.lower(),
                    "shortCombatTactic": e.shortCombatTactics.lower(),
                    "location": e.occurrence.lower(),
                    "description" : e.description.lower()
                    }
            #collection.insert_one(test)
            print(test)


# Running this script allows you to FILL the mongoDb database based on info on the ALCHEMY in the witcher 3 WIKI
# NOTE: It only looks for the enemies that are in the array Items[]
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
            print(test)
            #collection.insert_one(test)



# Function takes name and ingredients of the item you want to craft. It returns a string stating if its possible or not
# if it is not possible it'll return what items you are missing and how many ingredients of an item you are missing
def CheckIfIngredientsInInventory(name, tempIngredients):
    missingIngredients = []
    missingAmount = []
    #loop through the ingredients you need
    for i in range(0,len(tempIngredients)):
        foundIngredient = False
        currentTempEntry = tempIngredients[i].strip()
        currentTempAmount = currentTempEntry[0]
        currentTempIngredient = currentTempEntry[4:]
        #loop through ingredients you have
        for j in range(0, len(currentDatabaseItems)):
            currentEntry = currentDatabaseItems[j].strip()
            amount = currentEntry[0]
            ingredient = currentEntry[4:]
            #print(amount)
            if(ingredient == currentTempIngredient):
                foundIngredient = True
                if(amount < currentTempAmount):
                    tempInt = abs(int(amount) - int(currentTempAmount))
                    tempItem =  str(tempInt) + " x " + currentTempIngredient
                    missingAmount.append(tempItem)

        if foundIngredient == False:
            missingIngredients.append(currentTempIngredient)
    result = ""
    if missingIngredients == [] and missingAmount == []:
        #print("It is possible")
        result += "It is possible to craft " + name
    else:
        if missingIngredients != []:
            #print("You don't have these ingredients")
            #print(missingIngredients)
            result += "You don't have these ingredients " + str(missingIngredients)
        if missingAmount != []:
            #print("You are missing")
            #print(missingAmount)
            if missingIngredients != []:
                result += " and"
            result += " you are missing " + str(missingAmount)
    return result


"""
UNCOMMENT THE FOLLOWING LINES TO TEST THE CheckIfIngredientsInInventory METHOD
tempIngredient is double commented because one of them results in a positive result and the other in a negative result
"""
#TODO: A global array with all the items of the player needs to be made this is a placeholder one. It needs to follow this format
currentDatabaseItems = ['1 × Dwarven spirit   ', ' 1 × Werewolf mutagen ', ' 1 × Beggartick blossoms ', ' 1 × Hop umbels']

#The following lines are dummy data to show how to use the CheckIfIngredientInInverntory function.
# name = "Thunderbolt"

## When this line is uncommented you get a negative result
# #tempIngredient = ['3 × Dwarven spirit ', ' 4 × Werewolf mutagen ', ' 1 × Beggartick blossoms ', ' 1 × Hop umbels', ' 1 x trash']

# tempIngredient = ['1 × Dwarven spirit ', ' 1 × Werewolf mutagen ', ' 1 × Beggartick blossoms ', ' 1 × Hop umbels']
# print(CheckIfIngredientsInInventory(name, tempIngredient))
