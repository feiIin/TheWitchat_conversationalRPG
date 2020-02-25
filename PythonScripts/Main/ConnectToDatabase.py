from pymongo import MongoClient

# TRY TO CONNECT TO A LOCAL MONGODB DATABASE
try:
        client = MongoClient('localhost', 27017)
        print("SUCCESSFULLY FOUND DATABASE")
except:
        print("FAILED")
# Once it has successfully connected to a local mongodb database we set the database to convAgentDB (which is what we
# should name our local database holding all the information.
db = client.convAgentDB