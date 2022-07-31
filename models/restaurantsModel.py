import uuid
from config import db
from .entities import Restaurants
from flask import jsonify, request
from werkzeug.security import generate_password_hash

def get_all():
  rest = Restaurants.query.all()
  return jsonify({"Restaurants": [restaurants.to_json() for restaurants in rest]}), 200

def get_by_id(id):
  rest = Restaurants.query.get(id)
  if rest is None:
    return {"error": "Not found"}, 404
  return jsonify(rest.to_json())

def get_orders(current_rest, id):
  rest = Restaurants.query.get(id)
  if rest is None:
    return {"error": "Not found"}, 404
  data = rest.orders
  orders = []
  for order in data:
    orders.append(order.to_json())
  return jsonify(orders)

def insert():
  if request.is_json:
    body = request.get_json()
    hash_password = generate_password_hash(body["password"], method='sha256')
    res = Restaurants (
      public_id = str(uuid.uuid4()),
      name = body["name"],
      cnpj = body["cnpj"], 
      email = body["email"],
      password = hash_password,
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
      return {"error": "Not found"}, 404
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
    return {"message": "updated successfully"}, 200
  return {"error": "Request must be JSON"}, 415

def soft_delete(id):
  rest = Restaurants.query.get(id)
  if rest is None:
      return {"error": {"error": "Not found"}}, 404
  rest.active = False
  db.session.add(rest)
  db.session.commit()
  return {"message": "deleted successfully"}, 200


