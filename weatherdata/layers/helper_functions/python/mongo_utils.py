import pymongo
from boto3_toolkit import Boto3Utils

class MongoUtils:
    def __init__(self):
        self.config = Boto3Utils().get_secret(secret_name="WeatherPipelineSecrets")
        self.client = self.connect_to_mongo()

    def connect_to_mongo(self):
        try:
            client = pymongo.MongoClient(self.config['MONGODB_CONNECTION_STRING'])
            return client[self.config['MONGODB_DATABASE']]
        except KeyError as e:
            print(f"Missing configuration key: {e}")
            return None
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return None

    def insert_records(self, collection_name, data, many = False):
        try:
            collection = self.client[collection_name]
            if not many:
                result = collection.insert_one(data)
            elif many:
                result = collection.insert_many(data)
            return result.inserted_id
        except Exception as e:
            print(f"Error inserting data: {e}")
            return None

    def find_one(self, collection_name, key, value):
        try:
            collection = self.client[collection_name]
            result = collection.find({key: value})
            results = list(result)
            return results
        except Exception as e:
            print(f"Error finding data: {e}")
            return None
        
    def update_records(self, collection_name, query, update_data):
        try:
            collection = self.client[collection_name]
            result = collection.update_many(query, {'$set': update_data})
            print(f"Updated {result.modified_count} Records Successfully")
            return result.modified_count
        except Exception as e:
            print(f"Error updating data: {e}")
            return None