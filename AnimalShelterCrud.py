# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT =  31569
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    def __init__(self, user, password):#contructor with login
        HOST = 'nv-desktop-services.apporto.com'
        PORT =  31569
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,password,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
                
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary
            if result:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self,data ):
        if data is not None:
            return list(self.database.animals.find(data))
        else:
            raise Exception("Nothing to save, because data parameter is empty") 
            
# Update method to implement the U in CRUD.
#dataOld is filter
#dataNew is what is being set and how its being updated
#ex: collection.update({"Filter Attribute":"Filter Value"},{"$updateType":{"update Attribute":"update value"})
    def update(self, dataOld, dataNew):
        if dataOld is not None and dataNew is not None:
            self.database.animals.update_many(dataOld, dataNew)
            return True
        else:
            return False;
         
# Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_many(data)
        else:
            return False
