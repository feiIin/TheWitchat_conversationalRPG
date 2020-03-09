from ConnectToDatabase import *

# These are examples of how to query data from the database
# The following scripts need a name and an element.
# The name is the name of the enemy/item you want data from and the element in the database you want returned.

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

