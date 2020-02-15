from flask import Flask,request,make_response,jsonify
from api import login as loginAPI
import json
from flask_cors import CORS,cross_origin


app=Flask(__name__)
app.debug=True


@app.route('/login',methods=['POST'])
def logIn():
    data=request.json
    token=loginAPI.sendUserData(data["email"],data["password"])
    return jsonify(token)


