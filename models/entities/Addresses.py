from config import db

class Addresses(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  city = db.Column(db.String(50))
  state = db.Column(db.String(50))
  cep = db.Column(db.String(50))
  number = db.Column(db.Integer)
  neighborhood = db.Column(db.String(50))
  active = db.Column(db.Boolean, default=True)
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "city": self.city,
      "cep": self.cep,
      "number": self.number,
      "neighborhood": self.neighborhood,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }