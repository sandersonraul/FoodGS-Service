from flask import Blueprint
from controllers import addressesController

app=Blueprint('addresses', __name__)

@app.route("/addresses", methods=["GET"])
def get_addresses():
  return addressesController.get_all()

@app.route("/addresses/<int:id>", methods=["GET"])
def get_address_by_id(id):
  return addressesController.get_by_id(id)

@app.route("/addresses", methods=["POST"])
def insert_addr():
  return addressesController.insert()

@app.route("/addresses/<int:id>", methods=["PUT"])
def update_addr(id):
  return addressesController.update(id)

@app.route("/addresses/<int:id>", methods=["DELETE"])
def delete_address(id):
  return addressesController.delete(id) 