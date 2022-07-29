from config import db
from flask import jsonify, request

class Orders(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  descr = db.Column(db.String(50))
  value = db.Column(db.Numeric(17,2))
  restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
  address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"))
  active = db.Column(db.Boolean, default=True)
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "descr": self.descr,
      "value": self.value,
      "restaurant_id": self.restaurant_id,
      "address_id": self.address_id,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }

  def get_all():
    ords = Orders.query.all()
    return jsonify([ord.to_json() for ord in ords]), 200
 
  def get_by_id(id):
    order = Orders.query.get(id)
    if order is None:
      return "Not found", 404
    return jsonify(order.to_json())

  def get_order_restaurant(restaurant_id, order_id):
    order = Orders.query.filter_by(id = order_id, restaurant_id = restaurant_id).first()
    if order is None:
      return "Not found", 404
    return jsonify(order.to_json())
  
  def insert():
    if request.is_json:
      body = request.get_json()
      order = Orders (
        descr = body["descr"],
        value = body["value"],
        restaurant_id = body["restaurant_id"],
        address_id = body["address_id"]
      )
      db.session.add(order)
      db.session.commit()
      return jsonify(order.to_json()) , 201
    return {"error": "Request must be JSON"}, 415
  
  def update(id):
    if request.is_json:
      body = request.get_json()
      order = Orders.query.get(id)
      if order is None:
        return "Not found", 404
      if("descr" in body):
        order.descr = body["descr"]
      if("value" in body):
        order.value = body["value"]
      if("restaurant_id" in body):
        order.restaurant_id = body["restaurant_id"]
      if("address_id" in body):
        order.address_id = body["address_id"]
      db.session.add(order)
      db.session.commit()
      return "updated successfully", 200
    return {"error": "Request must be JSON"}, 415

  def soft_delete(id):
    order = Orders.query.get(id)
    if order is None:
        return "Not found", 404
    order.active = False
    db.session.add(order)
    db.session.commit()
    return "deleted successfully", 200
