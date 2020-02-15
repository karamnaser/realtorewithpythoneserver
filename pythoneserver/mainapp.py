from routes import apartmentroutes,cityroute,countryrout,imageroute,login,signup
from flask import Flask,request,jsonify
from database import db
from flask_cors import CORS,cross_origin
from api import apartment,cityapi,countryeapi,login,singupapi,imegesapi
import urllib.request

app=Flask(__name__,static_url_path ="/images",static_folder ='images')
app.config['CORS_HEADERS'] = 'Content-Type'
app.debug=True
CORS(app,resources={r"/foo": {"origins": "http://localhost:3000"}},supports_credentials=True)

@app.after_request
def after_request(response):
   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
   response.headers.add('Access-Control-Allow-Credentials', 'true')
   return response

@app.route("/apartments",methods=["GET"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def getApartments():
   return apartment.queryApartmentsFromMongo(request.args)


@app.route("/apartments",methods=["POST"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def sendData():
   apartment.sendApartmentData(request.files["file"],request.form)
   return "aprtmenmt saved succefuly"

@app.route('/apartments/<apartmentid>',methods=["PUT"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def updateData(apartmentid):
   print(apartmentid,request.get_json()["status"])
   apartment.changeApartmentState(db.Apartment.objects(id=apartmentid),request.get_json()["status"])
   return "aprtmenmt upgraded succefuly"

@app.route("/apartments/apartmentnumber")
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def getApartmentNumbers():
    numberofapartment=db.Apartment.objects.count()
    return jsonify(numberofapartment)

@app.route('/city/<countryname>',methods=["GET"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def getCityes(countryname):
   cites=cityapi.gitCity(countryname)
   return jsonify(cites)


@app.route('/login',methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def logIn():
    data=request.json
    token=login.sendUserData(data["email"],data["password"])
    if token:
        return jsonify(token),200
    else:
        return jsonify("faild to connect"),500

@app.route('/signup',methods=["POST"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def signUp():
    data=request.json
    singupapi.sendUserData(data["email"],data["password"],data["firstname"],data["lastname"])
    return "user succesfuly added"

@app.route('/country',methods=["GET"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def getCountry():
   countres=countryeapi.getCountry()
   return jsonify(countres)

@app.route('/imeges/<apartmentid>',methods=["GET"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def getApartmentImeges(apartmentid):
   imegs=imegesapi.gitImeges(apartmentid)
   return jsonify(imegs)

app.run()