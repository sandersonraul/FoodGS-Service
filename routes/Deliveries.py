from flask import Blueprint
from authentication import auth
from controllers import deliveriesController

app=Blueprint('deliveries', __name__)

@app.route("/deliveries", methods=["GET"])
@auth.token_required
def get_deliveries():
  return deliveriesController.get_all()

@app.route("/deliveries/<int:id>", methods=["GET"])
def get_delivery_by_id(id):
  return deliveriesController.get_by_id(id)

@app.route("/deliveries", methods=["POST"])
@auth.token_required
def insert_delivery():
  return deliveriesController.insert()

@app.route("/deliveries/<int:id>", methods=["PUT"])
def update_deliveries(id):
  return deliveriesController.update(id)