import jwt
from config import db, app
from .entities import Deliveries, Restaurants
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
    token = request.headers['x-access-token']
    try:
      data = jwt.decode(token, app.config["SECRET_KEY"], options={"verify_signature": False})
      rest = Restaurants.query.filter_by(public_id = data["public_id"]).first()
    except:
      return {"error": "Not found"}, 404
    deliv = Deliveries (
      customer = body["customer"],
      restaurant_id = rest.id

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

def delivered(id):
  deliv = Deliveries.query.get(id)
  if deliv is None:
    return {"error": "Not found"}, 404
  deliv.id = 2
  db.session.add(deliv)
  db.session.commit()
  return "updated successfully", 200