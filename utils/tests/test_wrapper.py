# First run mongod --dbpath=data/db to have the mongo client running
# To run this script locally, either uncomment the following
# or add to PYTHONPATH.

import sys
import os
script_location = os.getcwd()

sys.path.append('../')

from mongo_wrapper import MongoDBWrapper
import random

db_wrapper = MongoDBWrapper('ConversationalRPG')

x_id = "XYZ"
resource_id = "nm0000123"
content = ["abcsskldjgldjgldjglkdgjldgkfdlgk"]
resource = "..."
topic = "quest"

cached_trivia = {"x_id":x_id,
                 "resource_id":resource_id,
                 "content":content,
                 "resource":resource,
                 "topic":topic}

db_wrapper.put_item(cached_trivia)

item = db_wrapper.get_item("x_id",x_id)
print(item)

# Test if item is not in db
# item = db_wrapper.get_item("x_id",0)
if item:
    print(random.choice(item["content"]))
else:
    print("No content found")

# Indexing on resource id instead of x_id
# item = db_wrapper.get_item("resource_id",resource_id)
# print(item)

# field_to_be_indexed = (x_id,resource_id)
# db_wrapper.ensure_index(field_to_be_indexed)