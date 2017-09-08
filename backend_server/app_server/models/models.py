from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.fl

def addWork(author, header, price, body):
    works = db.works
    service_id = works.insert_one({'author': author, 'header': header, 'price': price, 'body': body}).inserted_id
    return service_id

def getWorks():
    works = db.works
    service = works.find()
    pprint.pprint(service)
    return service
