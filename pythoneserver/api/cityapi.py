from database import db
from mongoengine import *
import  json

clint=connect("realtore")

def gitCity(city):
    cites=db.Countrie.objects(name=city).values_list('cities').to_json()
    print(cites)
    return json.loads(cites)