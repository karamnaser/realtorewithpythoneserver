from database import db
from mongoengine import *
import json
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

client = connect("realtore")


def sendUserData(email,password):
    # print(generate_password_hash(password, method='pbkdf2:sha512'))
    user=db.Users.objects(email=email,password=password)
    if user:
        token={"email":user[0].email,"role":user[0].role}
        return token



