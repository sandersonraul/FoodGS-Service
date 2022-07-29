from config import create_app
from flask_cors import CORS
from controllers import restaurantsController, addressesController, couriersController, ordersController, deliveriesController

app = create_app()
cors = CORS(app)

@app.route("/addresses", methods=["GET"])
def get_addresses():
  return restaurantsController.get_all()

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

@app.route("/restaurants", methods=["GET"])
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

@app.route("/deliveries", methods=["GET"])
def get_deliveries():
  return deliveriesController.get_all()

@app.route("/deliveries/<int:id>", methods=["GET"])
def get_delivery_by_id(id):
  return deliveriesController.get_by_id(id)

@app.route("/deliveries", methods=["POST"])
def insert_delivery():
  return deliveriesController.insert()

@app.route("/deliveries/<int:id>", methods=["PUT"])
def update_deliveries(id):
  return deliveriesController.update(id)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8090)
