from config import db
from flask import jsonify, request

class Couriers(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String(50), unique=True)
  cpf = db.Column(db.String(30), unique=True)
  active = db.Column(db.Boolean, default=True)
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.password,
      "cpf": self.cpf,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }
  
  def get_all():
    couriers = Couriers.query.all()
    return jsonify([courier.to_json() for courier in couriers]), 200

  def get_by_id(id):
    couriers = Couriers.query.get(id)
    if couriers is None:
      return "Not found", 404
    return jsonify(couriers.to_json())

  def insert():
    if request.is_json:
      body = request.get_json()
      couriers = Couriers (
        name = body["name"],
        email = body["email"],
        password = body["password"],
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
        return "Not found", 404
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
        return "Not found", 404
    courier.active = False
    db.session.add(courier)
    db.session.commit()
    return "deleted successfully", 200