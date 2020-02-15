from database import db
from mongoengine import *
import  json

clint=connect("realtore")

def gitImeges(apartmentid):
    images=db.Apartment.objects(id=apartmentid).values_list('imeges').to_json()
    print(images)
    return json.loads(images)

