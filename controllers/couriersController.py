from models import couriersModel

def get_all():
  return couriersModel.get_all()

def get_by_id(id): 
  return couriersModel.get_by_id(id)

def insert():
  return couriersModel.insert()

def update():
  return couriersModel.update()

def delete(id):
  return couriersModel.soft_delete(id)