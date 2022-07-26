from config import db

class Orders(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  descr = db.Column(db.String(50))
  value = db.Column(db.Numeric(17,2))
  restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
  address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "descr": self.descr,
      "value": self.value,
      "restaurant_id": self.restaurant_id,
      "address_id": self.address_id,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }
