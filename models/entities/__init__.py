from .Couriers import Couriers
from .Deliveries import Deliveries
from .Restaurants import Restaurants
from config import db

__all__ = [
  'Couriers',
  'Deliveries',
  'Restaurants',
]

db.create_all()