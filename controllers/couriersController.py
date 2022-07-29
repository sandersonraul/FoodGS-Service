from models import Couriers

def get_all():
  return Couriers.get_all()

def get_by_id(id): 
  return Couriers.get_by_id(id)

def insert():
  return Couriers.insert()

def update():
  return Couriers.update()

def delete(id):
  return Couriers.soft_delete(id)