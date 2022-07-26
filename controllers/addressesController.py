from flask import jsonify, request
from models import Addresses
from config import db

def get_all():
  addrs = Addresses.query.all()
  return jsonify([addr.to_json() for addr in addrs]), 200

def get_by_id(id):
  addr = Addresses.query.get(id)
  if addr is None:
    return "Not founded", 404
  return jsonify(addr.to_json())

def insert():
  if request.is_json:
    address = request.get_json()
    addr = Addresses (
      city = address["city"],
      state = address["state"],
      cep = address["cep"],
      number = address["number"],
      neighborhood = address["neighborhood"]
    )
    db.session.add(addr)
    db.session.commit()
    return "created successfully", 201
  return {"error": "Request must be JSON"}, 415

# def update(id):
