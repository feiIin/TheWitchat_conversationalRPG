from pymongo import MongoClient

try:
        client = MongoClient('localhost', 27017)
        print("SUCCESSFULLY FOUND DATABASE")
except:
        print("FAILED")

db = client.convAgentDB