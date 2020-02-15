from flask import Flask,request,make_response,jsonify
from api import singupapi

app=Flask(__name__)
app.debug=True

@app.route('/signup',methods=["POST"])
def signUp():
    data=request.json
    singupapi.sendUserData(data["email"],data["password"],data["firstname"],data["lastname"])
    return "user succesfuly added"

