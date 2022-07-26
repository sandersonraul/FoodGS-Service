from config import db

class Deliveries(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
  courier_id = db.Column(db.Integer, db.ForeignKey('couriers.id'))
  status = db.Column(db.String(30), default="EM ANDAMENTO")
  created_at  = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def to_json(self):
    return {
      "id": self.id,
      "order_id": self.order_id,
      "courier_id": self.courier_id,
      "status": self.status,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }