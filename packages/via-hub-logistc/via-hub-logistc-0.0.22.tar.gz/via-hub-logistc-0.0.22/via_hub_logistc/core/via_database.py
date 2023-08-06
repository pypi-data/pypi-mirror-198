import pymongo
import random
import math

from pydoc import cli
from datetime import datetime

from robot.api.logger import info, debug, trace, console, error
from robot.api.deco import keyword
from robot.api import Error

class ViaMongo():

    def connect_to_database(self, strConnction):
        try:
            client = pymongo.MongoClient(f"mongodb://{strConnction}/")

            return client
        except Exception as e:
            raise Error(e)


    def disconnect_to_database(self, client):
        try:
            client.close()

            info("Connection has closed sucess")
        except Exception as e:
            raise Error(e)


    def find_all(self, client, baseName, collectionName):
        try:
            lstItems = []

            dataBase = client[baseName]

            collection = dataBase[collectionName]

            result = collection.find()

            for item in result:
                lstItems.append(item)

            info(lstItems)

            return lstItems
        except Exception as e:
            raise Error(e)


    def find_by_pameter(self, client, baseName, collectionName, parameter, value):
        try:
            dataBase = client[baseName]

            collection = dataBase[collectionName]

            for item in collection.find({parameter: value}):
                if item[parameter] == value:
                    info(item)
                    return item

            return None
        except Exception as e:
            raise Error(e)
