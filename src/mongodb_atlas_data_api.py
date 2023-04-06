import requests
import json

"""
    The MongoOperator class is used to operate the MongoDB Atlas Data API.
    The class is initialized with the following parameters:
    - data_api: The data API of the cluster, e.g. https://data-xxxxxxx.mongodb-api.com
    - access_key: The access key of the cluster, e.g. 12345678-1234-1234-1234-123456789012
    - data_source: The data source of the cluster, e.g. mongodb-atlas
    - database: The database to operate on
    - collection: The collection to operate on
    The class contains methods to operate the MongoDB Atlas Data API.
    The methods are:
    - find_one: Find a single document
    - find: Find multiple documents
    - insert_one: Insert a single document
    - insert_many: Insert multiple documents
    - update_one: Update a single document
    - update_many: Update multiple documents
    - delete_one: Delete a single document
    - delete_many: Delete multiple documents
    - aggregate: Aggregate documents
    The methods accept the following parameters:
    - filter: The query filter, e.g. {"name": "MongoDB"}
    - projection: The fields to return, e.g. {"name": 1, "_id": 0}
    - sort: The sort order, e.g. {"name": 1}
    - limit: The maximum number of documents to return, e.g. 1
    - skip: The number of documents to skip before returning, e.g. 1
    - document: The document to insert, e.g. {"name": "MongoDB"}
    - documents: The documents to insert, e.g. [{"name": "MongoDB"}, {"name": "MongoDB"}]
    - update: The update operations to perform, e.g. {"$set": {"name": "MongoDB"}}
    - upsert: Whether to insert a new document if no documents match the filter, e.g. True
    - pipeline: The aggregation pipeline, e.g. [{"$group": {"_id": "$name", "count": {"$sum": 1}}}]
"""

class MongoOperator:
        
    def __init__(self, data_api, access_key, data_source, database, collection):
        #If the provided data API is a full URL, use it as is. Otherwise, construct the URL.
        if("https" in data_api):
            self.base_url = f"{data_api}/action/"
        else:
            self.base_url = f"https://data.mongodb-api.com/app/{data_api}/endpoint/data/v1/action/"
        self.headers = {
            "Content-Type": "application/json",
            "api-key": access_key,
            "Accept": "application/json",
        }
        self.payload = {
            "dataSource": data_source,
            "database": database,
            "collection": collection,
        }

    def find_one(self, filter=None, projection=None):
        url = self.base_url + "findOne"
        payload = self.payload
        if projection:
            payload["projection"] = projection
        if filter:
            payload["filter"] = filter
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
        
    def find(self, filter=None, projection=None, sort=None, limit=None, skip=None):
        url = self.base_url + "find"
        payload = self.payload
        if projection:
            payload["projection"] = projection
        if filter:
            payload["filter"] = filter
        if sort:
            payload["sort"] = sort
        if limit:
            payload["limit"] = limit
        if skip:
            payload["skip"] = skip
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def insert_one(self, document):
        url = self.base_url + "insertOne"
        payload = self.payload
        payload["document"] = document
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def insert_many(self, documents):
        url = self.base_url + "insertMany"
        payload = self.payload
        payload["documents"] = documents
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def update_one(self, filter, update, upsert=None):
        url = self.base_url + "updateOne"
        payload = self.payload
        payload["filter"] = filter
        payload["update"] = update
        if upsert:
            payload["upsert"] = upsert
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def update_many(self, filter, update, upsert=None):
        url = self.base_url + "updateMany"
        payload = self.payload
        payload["filter"] = filter
        payload["update"] = update
        if upsert:
            payload["upsert"] = upsert
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def delete_one(self, filter):
        url = self.base_url + "deleteOne"
        payload = self.payload
        payload["filter"] = filter
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def delete_many(self, filter):
        url = self.base_url + "deleteMany"
        payload = self.payload
        payload["filter"] = filter
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
    
    def aggregate(self, pipeline):
        url = self.base_url + "aggregate"
        payload = self.payload
        payload["pipeline"] = pipeline
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()