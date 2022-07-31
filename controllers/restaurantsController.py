from models import restaurantsModel

def get_all():
  return restaurantsModel.get_all()

def get_by_id(id):
  return restaurantsModel.get_by_id(id)

def get_orders(current_rest, id):
  return restaurantsModel.get_orders(current_rest, id)

def insert():
  return restaurantsModel.insert()

def update(id):
  return restaurantsModel.update(id)

def delete(id): 
  return restaurantsModel.soft_delete(id)