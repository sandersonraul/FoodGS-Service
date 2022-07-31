from .Addresses import Addresses
from .Couriers import Couriers
from .Deliveries import Deliveries
from .Restaurants import Restaurants
from .Orders import Orders
from config import db

__all__ = [
  'Addresses',
  'Couriers',
  'Deliveries',
  'Restaurants',
  'Orders'
]

db.create_all()