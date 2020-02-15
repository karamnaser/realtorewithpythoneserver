from flask import Flask,request,jsonify
from api import cityapi
app=Flask(__name__)
app.debug=True

@app.route('/city/<countryname>',methods=["GET"])
def getCityes(countryname):
   cites=cityapi.gitCity(countryname)
   return jsonify(cites)

