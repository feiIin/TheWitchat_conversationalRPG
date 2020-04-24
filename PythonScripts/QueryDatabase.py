from ConnectToDatabase import *
def GetEnemyInfo(enemyName, nameOfElement):
    print("SYSTEM HAS FOUND KEYWORDS: " + enemyName + " AND " + nameOfElement)
    collection = db.Enemies
    if enemyName == "griffin":
        enemyName = "griffin (creature)"
    print(enemyName)
    myquery = {"name": enemyName}
    response = ""
    try:
        mydoc = collection.find(myquery)
        tempResult = str(mydoc[0][nameOfElement])
        response = tempResult
    except:
        print("ENEMY Entry invalid " + enemyName + "  "+ nameOfElement)
        response = "Entry invalid"
    return response

def GetAlchemyInfo(itemName, nameOfElement):
    print("SYSTEM HAS FOUND KEYWORDS: " + itemName + " AND " + nameOfElement)
    collection = db.Alchemy
    myquery = {"name": itemName}
    response = ""
    try:
        mydoc = collection.find(myquery)
        tempResult = str(mydoc[0][nameOfElement])
        response = tempResult
    except:
      #  print("ALCHEMY Entry invalid " + itemName + "  "+ nameOfElement)
        response = "Entry invalid"
    return response


def GetLocationInfo(LocationName, nameOfElement):
    print("SYSTEM HAS FOUND KEYWORDS: " + LocationName + " AND " + nameOfElement)
    collection = db.Locations

    myquery = {"name": LocationName}
    response = ""
    try:
        mydoc = collection.find(myquery)
        tempResult = str(mydoc[0][nameOfElement])
        response = tempResult
    except:
        print("ENEMY Entry invalid " + LocationName + "  "+ nameOfElement)
        response = "Entry invalid"
    return response

def GetCharacterInfo(CharacterName, nameOfElement):
    print("SYSTEM HAS FOUND KEYWORDS: " + CharacterName + " AND " + nameOfElement)
    collection = db.Characters

    myquery = {"name": CharacterName}
    response = ""
    try:
        mydoc = collection.find(myquery)
        tempResult = str(mydoc[0][nameOfElement])
        response = tempResult
    except:
        print("ENEMY Entry invalid " + CharacterName + "  "+ nameOfElement)
        response = "Entry invalid"
    return response

#
# try:
#         client = MongoClient('localhost', 27017)
#         print("FOUND")
# except:
#         print("FAILED")
#
# db = client.convAgentDB
#
# #GetEnemyInfo("Ghoul", "longCombatTactic")
# #GetAlchemyInfo("Swallow", "ingredients")
