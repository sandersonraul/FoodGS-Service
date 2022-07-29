from models import Addresses

def get_all():
  return Addresses.get_all()

def get_by_id(id):
  return Addresses.get_by_id(id)

def insert():
  return Addresses.insert()

def update(id):
  return Addresses.update(id)

def delete(id):
  return Addresses.soft_delete(id)