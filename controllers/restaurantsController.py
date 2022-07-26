from flask import jsonify, request
from models import Restaurants
from config import db

def get_all():
  rest = Restaurants.query.all()
  return jsonify([restaurants.to_json() for restaurants in rest]), 200

def get_by_id(id):
  rest = Restaurants.query.get(id)
  if rest is None:
    return "Not found", 404
  return jsonify(rest.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    res = Restaurants (
      name = body["name"],
      cnpj = body["cnpj"],
      email = body["email"],
      address_id = body["address_id"]
    )
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_json()) , 201
  return {"error": "Request must be JSON"}, 415

def update(id):
  if request.is_json:
    body = request.get_json()
    rest = Restaurants.query.get(id)
    if rest is None:
      return "Not found", 404
    if("name" in body):
      rest.name = body["name"]
    if("cpnj" in body):
      rest.cnpj = body["cnpj"]
    if("email" in body):
      rest.email = body["email"]
    if("active" in body):
      rest.active = body["active"]
    if("address_id" in body):
      rest.address_id = body["address_id"]
    db.session.add(rest)
    db.session.commit()
    return "updated successfully", 200
  return {"error": "Request must be JSON"}, 415
