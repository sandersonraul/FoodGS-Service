from config import create_app, db
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

@app.route("/restaurants",methods=['GET'])
def get_restaurants():
    return restaurantsController.get_all()

@app.route("/restaurants/<int:id>",methods=['GET'])
def get_restaurant_by_id(id):
  return restaurantsController.get_by_id(id)

@app.route("/restaurants", methods=["POST"])
def insert_restaurants():
  return restaurantsController.insert()

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8090)
  db.create_all = True