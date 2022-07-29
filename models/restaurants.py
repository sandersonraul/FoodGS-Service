from config import db
from flask import jsonify, request

class Restaurants(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  cnpj = db.Column(db.String(50))
  email = db.Column(db.String(50), unique=True)
  active = db.Column(db.Boolean, default=True)
  address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  orders = db.relationship('Orders', backref='restaurants')

  def to_json(self):
    return {
      "id": self.id,  
      "name": self.name,
      "cnpj": self.cnpj,
      "email": self.email,
      "active": self.active,
      "address_id": self.address_id,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }

  def get_all():
    rest = Restaurants.query.all()
    return jsonify([restaurants.to_json() for restaurants in rest]), 200

  def get_by_id(id):
    rest = Restaurants.query.get(id)
    if rest is None:
      return "Not found", 404
    return jsonify(rest.to_json())

  def get_orders(id):
    rest = Restaurants.query.get(id)
    if rest is None:
      return "Not found", 404
    data = rest.orders
    orders = []
    for order in data:
      orders.append(order.to_json())
    return jsonify(orders)
  
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

  def soft_delete(id):
    rest = Restaurants.query.get(id)
    if rest is None:
        return "Not found", 404
    rest.active = False
    db.session.add(rest)
    db.session.commit()
    return "deleted successfully", 200