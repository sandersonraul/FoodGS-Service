from flask import jsonify, request
from models import Restaurants
from config import db

def get_all():
  rest = Restaurants.query.all()
  return jsonify([restaurants.to_json() for restaurants in rest]), 200

def get_by_id(id):
  rest = Restaurants.query.get(id)
  if rest is None:
    return "Not founded", 404
  return jsonify(rest.to_json())

def insert():
  if request.is_json:
    restaurant = request.get_json()
    res = Restaurants (
      name = restaurant["name"],
      cnpj = restaurant["cnpj"],
      email = restaurant["email"],
      address_id = restaurant["address_id"]
    )
    db.session.add(res)
    db.session.commit()
    return jsonify(res.to_json()) , 201
  return {"error": "Request must be JSON"}, 415