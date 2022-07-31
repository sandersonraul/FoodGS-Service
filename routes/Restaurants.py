from flask import Blueprint
from controllers import restaurantsController, ordersController

app=Blueprint('restaurants', __name__)

@app.route('/restaurants', methods=["GET"])
def get_restaurants():
  return restaurantsController.get_all()

@app.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant_by_id(id):
  return restaurantsController.get_by_id(id)

@app.route("/restaurants/<int:id>/orders", methods=["GET"])
def get_restaurant_orders(id):
  return restaurantsController.get_orders(id)

@app.route("/restaurants/<int:restaurant_id>/<int:order_id>", methods=["GET"])
def get_order_restaurant(restaurant_id, order_id):
  return ordersController.get_order_restaurant(restaurant_id, order_id)

@app.route("/restaurants", methods=["POST"])
def insert_restaurants():
  return restaurantsController.insert()

@app.route("/restaurants/<int:id>", methods=["PUT"])
def update_restaurant(id):
  return restaurantsController.update(id)

@app.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
  return restaurantsController.delete(id)