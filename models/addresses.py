from config import db
from flask import jsonify, request

class Addresses(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  city = db.Column(db.String(50))
  state = db.Column(db.String(50))
  cep = db.Column(db.String(50))
  number = db.Column(db.Integer)
  neighborhood = db.Column(db.String(50))
  active = db.Column(db.Boolean, default=True)
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "city": self.city,
      "cep": self.cep,
      "number": self.number,
      "neighborhood": self.neighborhood,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }

  def get_all():
    addrs = Addresses.query.all()
    return jsonify([addr.to_json() for addr in addrs]), 200

  def get_by_id(id):
    addr = Addresses.query.get(id)
    if addr is None:
      return "Not found", 404
    return jsonify(addr.to_json())

  def insert():
    if request.is_json:
      body = request.get_json()
      addr = Addresses (
        city = body["city"],
        state = body["state"],
        cep = body["cep"],
        number = body["number"],
        neighborhood = body["neighborhood"]
      )
      db.session.add(addr)
      db.session.commit()
      return "created successfully", 201
    return {"error": "Request must be JSON"}, 415

  def update(id):
    if request.is_json:
      body = request.get_json()
      addr = Addresses.query.get(id)
      if addr is None:
        return "Not found", 404
      if("city" in body):
        addr.city = body["city"]
      if("state" in body):
        addr.state = body["state"]
      if("cep" in body):
        addr.cep = body["cep"]
      if("number" in body):
        addr.number = body["number"]
      if("neighborhood" in body):
        addr.neighborhood = body["neighborhood"]
      db.session.add(addr)
      db.session.commit()
      return "updated successfully", 200
    return {"error": "Request must be JSON"}, 415

  def soft_delete(id):
    addr = Addresses.query.get(id)
    if addr is None:
        return "Not found", 404
    addr.active = False
    db.session.add(addr)
    db.session.commit()
    return "deleted successfully", 200