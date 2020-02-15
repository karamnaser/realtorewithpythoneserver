from flask import Flask,request
from api import  apartment as API
from database import db


app=Flask(__name__)
app.debug=True





@app.route("/apartments",methods=["GET"])
def getApartments():
   return API.queryApartmentsFromMongo(request.args)

@app.route("/apartments",methods=["POST"])
def sendData():
   API.sendApartmentData(request.files["file"],request.form)
   return "aprtmenmt saved succefuly"

@app.route('/apartments/<apartmentid>',methods=["PUT"])
def updateData(apartmentid):
   print(apartmentid,request.get_json()["status"])
   API.changeApartmentState(db.Apartment.objects(id=apartmentid),request.get_json()["status"])
   return "aprtmenmt upgraded succefuly"


