import pymongo
import pycountry
import geonamescache
from mongoengine import *
import json
import datetime
import requests



# client = connect("realtore")
# data=requests.get("https://raw.githubusercontent.com/shivammathur/countrycity/master/data/geo.json").json()



class Countrie(Document):
    name=StringField()
    cities=ListField()

class Roles(Document):
    type=StringField()



class Apartment(Document):
        country=StringField(required=True)
        city=StringField(required=True)
        address = StringField(required=True)
        price = IntField(required=True)
        numberofrooms = IntField()
        numberofbaths = IntField()
        sqft = IntField()
        ctreated_on = DateField(default=datetime.datetime.now())
        description = StringField()
        sale_status = StringField()
        availability = StringField(default="avilabile")
        property_type = StringField()
        imeges = ListField()
        main_img=StringField()
        status=StringField(default="pending")

class Users(Document):
    role=StringField()
    apartments=ListField()
    firstname=StringField(required=True)
    lastname=StringField(required=True)
    email=EmailField(required=True)
    password=StringField(required=True)
    phone=IntField()
    status="active"




