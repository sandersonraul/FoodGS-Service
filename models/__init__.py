from .addresses import Addresses
from .restaurants import Restaurants
from .orders import Orders
from .couriers import Couriers
from .deliveries import Deliveries
from config import db

__all__ = [
  'Addresses',
  'Restaurants',
  'Orders',
  'Couriers',
  'Deliveries'
]

db.create_all()