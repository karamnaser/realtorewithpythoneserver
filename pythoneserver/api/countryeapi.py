from database import db
from mongoengine import *
import  json

clint=connect("realtore")

def getCountry():
    countres=db.Countrie.objects().values_list('name').to_json()
    print(countres)
    return json.loads(countres)