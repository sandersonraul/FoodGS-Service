from flask import Blueprint
from controllers import restaurantsController
from authentication import auth

app=Blueprint('restaurants', __name__)

@app.route('/restaurants', methods=["GET"])
@auth.token_required
def get_restaurants():
  return restaurantsController.get_all()

@app.route("/restaurants/<int:id>", methods=["GET"])
@auth.token_required
def get_restaurant_by_id(id):
  return restaurantsController.get_by_id(id)

@app.route("/restaurants/<int:id>/orders", methods=["GET"])
@auth.token_required
def get_restaurant_orders(current_rest, id):
  return restaurantsController.get_orders(current_rest, id)

@app.route("/restaurants", methods=["POST"])
def insert_restaurants():
  return restaurantsController.insert()

@app.route("/restaurants/<int:id>", methods=["PUT"])
@auth.token_required
def update_restaurant(id):
  return restaurantsController.update(id)

@app.route("/restaurants/<int:id>", methods=["DELETE"])
@auth.token_required
def delete_restaurant(id):
  return restaurantsController.delete(id)
