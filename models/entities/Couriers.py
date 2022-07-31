from config import db

class Couriers(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String(50), unique=True)
  cpf = db.Column(db.String(30), unique=True)
  active = db.Column(db.Boolean, default=True)
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.password,
      "cpf": self.cpf,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }