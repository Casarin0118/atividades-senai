from flask import Blueprint
from flask_jwt_extended import create_access_token
from dotenv import load_dotenv
import os

load_dotenv()

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    token = create_access_token(identity='usuario')
    return {'token': token}