from api import serachbuilder as sb
from mongoengine import *
from database import db
import json
import os

client = connect("realtore")

def queryApartmentsFromMongo(searchparams):
    data=json.loads(json.dumps(searchparams))
    if data.get("price"):
        data["price"]=int(data["price"])

    if data.get("numberofrooms"):
        data["numberofrooms"] = int(data["numberofrooms"])

    if data.get("numberofbaths"):
        data["numberofbaths"] = int(data["numberofbaths"])

    serachbuilder = sb.SearchBuilder()
    queryparams = json.dumps(serachbuilder.id(data.get("id",""))
                             .city(data.get("city",""))
                             .price(data.get("price",""))
                             .roomnumber(data.get("numberofrooms",""))
                             .salestate(data.get("salestatus",""))
                             .status(data.get("status",""))
                             .avilabilty(data.get("avilabilty",""))
                             .country(data.get("country",""))
                             .bathnumber(data.get("numberofbaths",""))
                             .build())

    print(queryparams)
    apartments=db.Apartment.objects(__raw__=json.loads(queryparams)).to_json()
    return apartments

def sendApartmentData(file,form):
    db.Apartment(country= form["country"],city=form["city"],address=form["address"]
                 ,price=form["price"],numberofrooms=form["numberofrooms"]
                 ,numberofbaths=form["numberofbaths"],sqft=form["sqft"]
                 ,description=form["description"],sale_status=form["salestatuse"]
                 ,property_type=form["propertytype"],main_img=file.filename).save()
    file.save(os.path.join("C:\\Users\\karam\\PycharmProjects\\pythoneserver\\images\\apartment",file.filename))

def changeApartmentState(apartment,state):
    print(apartment[0].id)
    apartment[0].update(set__status=state)
    print("Changed")
    apartment[0].save()

