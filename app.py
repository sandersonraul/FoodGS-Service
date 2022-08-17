from config import app
from flask_cors import CORS
from routes import Auth, Couriers, Restaurants, Deliveries

cors = CORS(app)

if __name__ == '__main__':

  app.register_blueprint(Auth.app)
  app.register_blueprint(Couriers.app)
  app.register_blueprint(Restaurants.app)
  app.register_blueprint(Deliveries.app)
  app.run(debug=True, host="0.0.0.0", port=8090)