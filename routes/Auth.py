from flask import Blueprint
from authentication import auth

app=Blueprint('login', __name__)

@app.route("/login/restaurants" , methods=["GET"])
def login():
  return auth.login()