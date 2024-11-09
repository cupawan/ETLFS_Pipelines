import os
import pymongo


class MongoUtils:
    def __init__(self):
        self.client = self.connect_to_mongo()

    def connect_to_mongo(self):
        client = pymongo.MongoClient(
            os.environ["MongodbConnectionString"].replace("=", ":")
        )
        return client[os.environ["MongodbDatabase"]]

    def insert_records(self, collection_name, data, many=False):
        collection = self.client[collection_name]
        if not many:
            result = collection.insert_one(data)
        elif many:
            result = collection.insert_many(data)
        return result.inserted_id

    def find_records_by_query(self, collection_name, query):
        collection = self.client[collection_name]
        result = collection.find_one(query)
        return result

    def find_by_key_value(self, collection_name, key, value):
        collection = self.client[collection_name]
        result = collection.find({key: value})
        results = list(result)
        return results

    def update_record(self, collection_name, query, update_data, upsert):
        collection = self.client[collection_name]
        result = collection.update_one(query, {"$set": update_data}, upsert=upsert)
        print(f"Updated {result.modified_count} Records Successfully")
        return result.modified_count

    def replace_one(self, collection_name, query, upsert=True):
        collection = self.client[collection_name]
        result = collection.replace_one(query, upsert=upsert)
        return result.modified_count
