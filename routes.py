from config import create_app
from flask_cors import CORS
from controllers import restaurantsController, addressesController

app = create_app()
cors = CORS(app)
  
@app.route("/addresses",methods=["GET"])
def get_addresses():
  return addressesController.get_all()

@app.route("/addresses/<int:id>" , methods=["GET"])
def get_address_by_id(id):
  return addressesController.get_by_id(id)

@app.route("/addresses", methods=["POST"])
def insert_addr():
  return addressesController.insert()

@app.route("/addresses/<int:id>" , methods=["PUT"])
def update_addr(id):
  return addressesController.update(id)

@app.route("/restaurants",methods=["GET"])
def get_restaurants():
    return restaurantsController.get_all()

@app.route("/restaurants/<int:id>",methods=["GET"])
def get_restaurant_by_id(id):
  return restaurantsController.get_by_id(id)

@app.route("/restaurants", methods=["POST"])
def insert_restaurants():
  return restaurantsController.insert()

@app.route("/restaurants/<int:id>",methods=["PUT"])
def update_restaurant(id):
  return restaurantsController.update(id)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8090)