from models import addressesModel

def get_all():
  return addressesModel.get_all()

def get_by_id(id):
  return addressesModel.get_by_id(id)

def insert():
  return addressesModel.insert()

def update(id):
  return addressesModel.update(id)

def delete(id):
  return addressesModel.soft_delete(id)