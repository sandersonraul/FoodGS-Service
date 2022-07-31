from flask import Blueprint
from auth import restaurants_login

app=Blueprint('login', __name__)

@app.route("/login/restaurants" , methods=["GET"])
def login():
  return restaurants_login()