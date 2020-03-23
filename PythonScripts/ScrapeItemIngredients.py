from bs4 import BeautifulSoup
from requests import get
import re

items = ["White Raffard's Decoction","Swallow","White Honey","Ekhidna decoction","Troll decoction" ,"Ekimmara decoction","Grave hag decoction",
         "Thunderbolt","Petri's Philter","Black Blood","Tawny Owl", "Maribor Forest", "Leshen decoction", "Nekker warrior decoction",
         "Katakan decoction", "Ancient leshen decoction", "Alghoul decoction", "Basilisk decoction", "Chort decoction",
         "Doppler decoction", "Foglet decoction", "Forktail decocion", "Succubus decoction", "Water hag decoction",
         "Wyvern decoction", "Full Moon", "Golden Oriole", "Blizzard", "Griffin decoction", "Reliever's decoction",
         "Earth elemental decoction", "Arachas decoction", "Nightwraith decoction", "Noonwraith decoction", "Cat_(potion)",
         "Fiend decoction", "Cockatrice decoction", "Werewolf decoction", "Killer whale"]

for x in items:
    url = 'https://witcher.fandom.com/wiki/' + x
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    index = 0
    skip = False


    print("==============")
    if html_soup.find(id ="The_Witcher_3:_Wild_Hunt") is None:
        Ingredients = html_soup.find("h2", class_="pi-item pi-item-spacing pi-title")
        if str(Ingredients) == "None":
            continue
        # name
        print(html_soup.find("h1").text)
        Ingredients = html_soup.find("h2", class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
        Ingredients = Ingredients.findNext("h2",class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
        Ingredients = Ingredients.findNext("h2",class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
        info = Ingredients
        Ingredients = Ingredients.findNext("h3").findNext("div")
        #Effect
        print(Ingredients.text)

        info = Ingredients.findNext("h2",class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
        Ingredients = info.findNext("h3").findNext("h3").findNext("div")
        finalText = re.sub('<.*?>', ' ', str(Ingredients))
        finalText = re.sub(' +', ' ',finalText)
        #Ingredients needed
        #print(finalText)
        #ADDED SHIT
        test = ""
        counter = 0
        for char in finalText.strip():
            if char.isdigit() and counter == 1:
                char = ", " + char
            test = test + char
            counter = 1
        print(test)
    else:
        skip = True

        # text = ""
        # while text != "Attributes":
        #     Ingredients = html_soup.findNext("h2", class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
        #     text = Ingredients.text
        # print(Ingredients)



    if skip is True:
        # name
        print(html_soup.find("h1").text)
        Ingredients = html_soup.find(id ="The_Witcher_3:_Wild_Hunt").parent
        Ingredients = Ingredients.findNext("h2", class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")

        info = Ingredients
        text = ""
        while text != "Attributes":
            Ingredients = Ingredients.findNext("h2", class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
            text = Ingredients.text

        Ingredients = Ingredients.findNext("h3")
        text = Ingredients.text
        while text != "Effect(s)":
            Ingredients = Ingredients.findNext("h3")
            text = Ingredients.text

        rawdata = str(Ingredients.nextSibling.nextSibling)
        finalText = re.sub('<.*?>', ' ', rawdata)
        finalText = re.sub(' +', ' ', finalText)
        #effects
        print(finalText)

    ###

        Ingredients = info
        while text != "Alchemy":
            Ingredients = Ingredients.findNext("h2", class_="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background")
            text = Ingredients.text

        Ingredients = Ingredients.findNext("h3")
        text = Ingredients.text
        while text != "Ingredients":
            Ingredients = Ingredients.findNext("h3")
            text = Ingredients.text

        rawdata = str(Ingredients.nextSibling.nextSibling)
        finalText = re.sub('<.*?>', ' ', rawdata)
        finalText = re.sub(' +', ' ',finalText)
        #ingredients needed
        print(finalText)

