from config import db
from .entities import Couriers
from flask import jsonify, request
from werkzeug.security import generate_password_hash
  
def get_all():
  couriers = Couriers.query.all()
  return jsonify([courier.to_json() for courier in couriers]), 200

def get_by_id(id):
  couriers = Couriers.query.get(id)
  if couriers is None:
    return {"error": "Not found"}, 404
  return jsonify(couriers.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    hash_password = generate_password_hash(body["password"], method='sha256')
    couriers = Couriers (
      name = body["name"],
      email = body["email"],
      password = hash_password,
      cpf = body["cpf"],
    )
    db.session.add(couriers)
    db.session.commit()
    return jsonify(couriers.to_json()), 201
  return {"error": "Request must be JSON"}, 415

def update(id):
  if request.is_json:
    body = request.get_json()
    courier = Couriers.query.get(id)
    if courier is None:
      return {"error": "Not found"}, 404
    if("name" in body):
      courier.name = body["name"]
    if("email" in body):
      courier.email = body["email"]
    if("cpf" in body):
      courier.cpf = body["cpf"]
    db.session.add(courier)
    db.session.commit()
    return "updated successfully", 200
  return {"error": "Request must be JSON"}, 415

def soft_delete(id):
  courier = Couriers.query.get(id)
  if courier is None:
      return {"error": "Not found"}, 404
  courier.active = False
  db.session.add(courier)
  db.session.commit()
  return "deleted successfully", 200

