from flask import Blueprint
from auth import login

app=Blueprint('login', __name__)

@app.route("/login/restaurants" , methods=["GET"])
def login():
  return login()