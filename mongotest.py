import pymongo
client = pymongo.MongoClient("mongodb+srv://mangodb:goal12l@cluster0.ix39k.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Prasad",
    "email" : "studyfor12@yahoo.com",
    "surname" : "hero"
}

db1 = client['mongotest']
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )