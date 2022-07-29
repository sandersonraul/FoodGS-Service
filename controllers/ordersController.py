from models import Orders

def get_all():
  return Orders.get_all()

def get_by_id(id):
  return Orders.get_by_id(id)

def get_order_restaurant(restaurant_id, order_id):
  return Orders.get_order_restaurant(restaurant_id, order_id)

def insert():
  return Orders.insert()
 
def update(id):
  return Orders.update(id)

def delete(id):
  return Orders.soft_delete(id)