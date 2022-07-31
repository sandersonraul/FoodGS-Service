from models import deliveriesModel

def get_all():
  return deliveriesModel.get_all()

def get_by_id(id):
  return deliveriesModel.get_by_id(id)

def insert():
  return deliveriesModel.insert()

def update(id):
  return deliveriesModel.update(id)
 

  

