from models import Deliveries

def get_all():
  return Deliveries.get_all()

def get_by_id(id):
  return Deliveries.get_by_id(id)

def insert():
  return Deliveries.insert()

def update(id):
  return Deliveries.update(id)
 

  

