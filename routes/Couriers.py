from flask import Blueprint
from controllers import couriersController

app=Blueprint('couriers', __name__)

@app.route("/couriers", methods=["GET"])
def get_couriers():
  return couriersController.get_all()

@app.route("/couriers/<int:id>", methods=["GET"])
def get_courier_by_id(id):
  return couriersController.get_by_id(id)

@app.route("/couriers", methods=["POST"])
def insert_courier():
  return couriersController.insert()

@app.route("/couriers/<int:id>", methods=["PUT"])
def update_courier(id):
  return couriersController.update(id)

@app.route("/couriers/<int:id>", methods=["DELETE"])
def delete_courier(id):
  return couriersController.delete(id)