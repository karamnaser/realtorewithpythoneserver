from flask import Flask,request,jsonify
from api import imegesapi
app=Flask(__name__)
app.debug=True

@app.route('/imeges/<apartmentid>',methods=["GET"])
def getApartmentImeges(apartmentid):
   imegs=imegesapi.gitImeges(apartmentid)
   return jsonify(imegs)

