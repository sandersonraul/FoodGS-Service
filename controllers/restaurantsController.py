from models import Restaurants

def get_all():
  return Restaurants.get_all()

def get_by_id(id):
  return Restaurants.get_by_id(id)

def get_orders(id):
  return Restaurants.get_orders(id)

def insert():
  return Restaurants.insert()

def update(id):
  return Restaurants.update(id)

def delete(id): 
  return Restaurants.soft_delete(id)