from pymongo import MongoClient
import json

try:
        client = MongoClient('localhost', 27017)
        print("FOUND")
except:
        print("FAILED")

db = client.convAgentDB


def GetEnemyInfo(enemyName, nameOfElement):
    collection = db.Enemies
    myquery = {"name": enemyName}
    try:
        mydoc = collection.find(myquery)
        tempResult = str(mydoc[0][nameOfElement])
        print(tempResult)
    except:
        print("Entry invalid")

def GetAlchemyInfo(itemName, nameOfElement):
    collection = db.Alchemy
    myquery = {"name": itemName}
    try:
        mydoc = collection.find(myquery)
        tempResult = str(mydoc[0][nameOfElement])
        print(tempResult)
    except:
        print("Entry invalid")

GetEnemyInfo("Ghoul", "longCombatTactic")
GetAlchemyInfo("Swallow", "ingredients")
