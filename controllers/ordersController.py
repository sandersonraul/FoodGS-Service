from models import ordersModel

def get_all():
  return ordersModel.get_all()

def get_by_id(id):
  return ordersModel.get_by_id(id)

def get_order_restaurant(restaurant_id, order_id):
  return ordersModel.get_order_restaurant(restaurant_id, order_id)

def insert():
  return ordersModel.insert()
 
def update(id):
  return ordersModel.update(id)

def delete(id):
  return ordersModel.soft_delete(id)