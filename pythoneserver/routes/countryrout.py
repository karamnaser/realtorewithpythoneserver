from flask import Flask,request,jsonify
from api import countryeapi
app=Flask(__name__)
app.debug=True

@app.route('/country',methods=["GET"])
def getCountry():
   countres=countryeapi.getCountry()
   return jsonify(countres)

