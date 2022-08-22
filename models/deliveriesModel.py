import jwt
from config import db, app
from .entities import Deliveries, Couriers
from flask import jsonify, request

def get_all():
  deliv = Deliveries.query.all()
  return jsonify([delivery.to_json() for delivery in deliv]), 200

def get_by_id(id):
  deliv = Deliveries.query.get(id)
  if deliv is None:
    return {"error": "Not found"}, 404
  return jsonify(deliv.to_json())

def insert():
  if request.is_json:
    body = request.get_json()
    deliv = Deliveries (
      order_id = body["order_id"],
      courier_id = body["courier_id"],
      status = body["status"]
    )
    db.session.add(deliv)
    db.session.commit()
    return jsonify(deliv.to_json()) , 201
  return {"error": "Request must be JSON"}, 415

def update(id):
  if request.is_json:
    body = request.get_json()
    deliv = Deliveries.query.get(id)
    if deliv is None:
      return {"error": "Not found"}, 404
    if("order_id" in body):
      deliv.order_id = body["order_id"]
    if("courier_id" in body):
      deliv.courier_id = body["courier_id"]
    if("status" in body):
      deliv.status = body["status"]
    db.session.add(deliv)
    db.session.commit()
    return "updated successfully", 200
  return {"error": "Request must be JSON"}, 415


def accept_delivery(id):
  token = request.headers['x-access-token']
  try:
    data = jwt.decode(token, app.config["SECRET_KEY"], options={"verify_signature": False})
    courier = Couriers.filter_by(email=data['email']).first() 
    deliv = Deliveries.query.get(id)
    deliv.courier_id = courier.id
    deliv.status = 1
    db.session.add(deliv)
    db.session.commit()
  except:
    return {"Error": "not found"}, 404
  return {"OK"}, 200