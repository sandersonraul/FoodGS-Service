from flask import Blueprint
from authentication import auth
from controllers import couriersController

app=Blueprint('couriers', __name__)

@app.route("/couriers", methods=["GET"])
@auth.token_required
def get_couriers():
  return couriersController.get_all()

@app.route("/couriers/<int:id>", methods=["GET"])
@auth.token_required
def get_courier_by_id(id):
  return couriersController.get_by_id(id)

@app.route("/couriers", methods=["POST"])
def insert_courier():
  return couriersController.insert()

@app.route("/couriers/<int:id>", methods=["PUT"])
@auth.token_required
def update_courier(id):
  return couriersController.update(id)

@app.route("/couriers/<int:id>", methods=["DELETE"])
@auth.token_required
def delete_courier(id):
  return couriersController.delete(id)