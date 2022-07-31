from flask import Blueprint
from controllers import ordersController

app=Blueprint('orders', __name__)

@app.route("/orders", methods=["GET"])
def get_orders():
  return ordersController.get_all()

@app.route("/orders/<int:id>", methods=["GET"])
def get_order_by_id(id):
  return ordersController.get_by_id(id)

@app.route("/orders", methods=["POST"])
def insert_order():
  return ordersController.insert()

@app.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):
  return ordersController.update(id)

@app.route("/orders/<int:id>", methods=["DELETE"])
def delete_order(id):
  return ordersController.delete(id)