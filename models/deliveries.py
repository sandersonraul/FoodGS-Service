from config import db
from flask import jsonify, request

class Deliveries(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
  courier_id = db.Column(db.Integer, db.ForeignKey('couriers.id'))
  status = db.Column(db.String(30), default="EM ANDAMENTO")
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "order_id": self.order_id,
      "courier_id": self.courier_id,
      "status": self.status,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }

  def get_all():
    deliv = Deliveries.query.all()
    return jsonify([delivery.to_json() for delivery in deliv]), 200
 
  def get_by_id(id):
    deliv = Deliveries.query.get(id)
    if deliv is None:
      return "Not found", 404
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
        return "Not found", 404
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
  