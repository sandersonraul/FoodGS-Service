from config import db

class Restaurants(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.String(50), unique=True)
  name = db.Column(db.String(50))
  cnpj = db.Column(db.String(50))
  email = db.Column(db.String(50), unique=True)
  active = db.Column(db.Boolean, default=True)
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  deliveries = db.relationship('Deliveries', backref='restaurants')

  def to_json(self):
    return {
      "id": self.id, 
      "public_id": self.public_id,
      "name": self.name,
      "cnpj": self.cnpj,
      "email": self.email,
      "active": self.active,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }