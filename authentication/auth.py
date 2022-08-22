import jwt
import datetime
from config import app
from functools import wraps
from models import entities
from flask import jsonify, make_response, request
from werkzeug.security import check_password_hash

def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs): 
    token = None  
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']
    if not token:
        return jsonify({'message' : 'Token is missing!'}), 401
    try: 
        data = jwt.decode(token, app.config['SECRET_KEY'], options={'verify_signature': False})
    except:
        return jsonify({'message' : 'Token is invalid!'}), 401
    return f( *args, **kwargs)
  return decorated

def login():
  auth = request.authorization
  if not auth or not auth.username or not auth.password:
    return make_response('Could not verify', 401, {'Error': 'Login required'})
  courier  = entities.Couriers.query.filter_by(email=auth.username).first_or_404()
  
  if check_password_hash(courier.password, auth.password):
    payload = {
    'public_id': courier.email,
    'exp' : datetime.datetime.utcnow() 
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'])
    return jsonify({'access_token': token}, token) 
  return {'Error': 'password incorret'} 