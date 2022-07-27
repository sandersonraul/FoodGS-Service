from flask import jsonify, request
from models import Orders
from config import db
 
def get_all():
  ords = Orders.query.all()
  return jsonify([ord.to_json() for ord in ords]), 200
 
def get_by_id(id):
  ord = Orders.query.get(id)
  if ord is None:
    return "Not found", 404
  return jsonify(ord.to_json())
 
def insert():
  if request.is_json:
    body = request.get_json()
    ord = Orders (
      descr = body["descr"],
      value = body["value"],
      restaurant_id = body["restaurant_id"],
      address_id = body["address_id"]
    )
    db.session.add(ord)
    db.session.commit()
    return jsonify(ord.to_json()) , 201
  return {"error": "Request must be JSON"}, 415
 
def update(id):
  if request.is_json:
    body = request.get_json()
    ord = Orders.query.get(id)
    if ord is None:
      return "Not found", 404
    if("descr" in body):
      ord.descr = body["descr"]
    if("value" in body):
      ord.value = body["value"]
    if("restaurant_id" in body):
      ord.restaurant_id = body["restaurant_id"]
    if("address_id" in body):
      ord.address_id = body["address_id"]
    db.session.add(ord)
    db.session.commit()
    return "updated successfully", 200
  return {"error": "Request must be JSON"}, 415
