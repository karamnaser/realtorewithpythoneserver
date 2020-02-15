from database import db
from mongoengine import *
import  json

client=connect("realtore")

def sendUserData(email,password,firstname,lastname):
    db.Users(email=email,password=password,
             firstname=firstname
             ,lastname=lastname,role="user").save()
