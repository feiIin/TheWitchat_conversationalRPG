# Adapted from Alana code

import json
import os

import sys
from pymongo import MongoClient
from retrying import retry


class MongoDBWrapper(object):
    """
    ---------------
    MongoDB wrapper
    ---------------
    1) Install mongodb (sudo apt-get install mongodb)
    2) Create the folder data/db in which the data will be stored (mkdir -p data/db)
    3) Start the db server (mongod --dbpath=path_to_data_folder)
    (optional) If you want to use GUI to check on the data you can use Robo3T (https://robomongo.org/download)
    If you want to use the shell take a look at https://docs.mongodb.com/manual/mongo/
    ---------------
    Uses the connection properties from mongo_info.json.
    Add default primary keys to mongo_default_keys.json. Bare in mind that "default key" is just a formalism in
    mongodb since it actually creates it's own primary key in the background for each item in the form of e.g.
    "_id" : ObjectId("5b5dc4e2f6728f72da016c8c") which we should not try to use. Thus by primary key I mean
    the first indexable field (to be on par with DynamoDB).
    By default the default primary keys are being indexed. If more need to be added to the index, use the
    ensure_index function like 'ensure_index(field_to_be_indexed)'
    """
    def __init__(self, in_table_name):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources/mongo_info.json')) as info:
            data = json.load(info)

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources/mongo_default_keys.json')) as kk:
            keys = json.load(kk)

        self.t_name = in_table_name
        self._db_name = data["database_name"]
        self._host = data["host"]
        self._port = data["port"]

        # Dict of default primary keys (more can be indexed using the ensure_index function
        self.schema = keys

        try:
            client = MongoClient(self._host, int(self._port))
            print(client)
        except ValueError as e:
            print("'%s' is not a valid port number." % self._port)
            print(e)
            sys.exit(1)

        self.table = init_dynamodb_table(client, in_table_name, db_name=self._db_name)

    def get_size(self):
        return self.table.item_count

    def is_empty(self):
        return self.get_size() == 0

    @retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=1)
    def put_item(self, in_item):
        self.table.update(
            {
                self.schema[self.t_name]: in_item[self.schema[self.t_name]]
            },
            in_item,
            upsert=True
        )
        self.table.ensure_index(self.schema[self.t_name])

    @retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=2)
    def get_item(self, *args):
        """
        Retrieves an item from the mongodb. Can either receive a single argument (primary key) or
        two arguments (field, item) if more than 1 fields have been added to the index
        :param args: Either <item> or <field, item>.
        :return: The enty based on the index provided
        """
        if len(args) == 1:
            item = self.table.find_one({self.schema[self.t_name]: args[0]})
        elif len(args) == 2:
            item = self.table.find_one({args[0]: args[1]})
        else:
            raise AttributeError('Max of 2 arguments can be accepted')
        return item

    def ensure_index(self, indexable_key):
        self.table.ensure_index(indexable_key)


def init_dynamodb_table(client, in_table_name, db_name):
    db = client[db_name]

    return db[in_table_name]