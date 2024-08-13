# authentication.py
from werkzeug.security import generate_password_hash, check_password_hash

users = {}

def register_user(username, master_password):
    hashed_password = generate_password_hash(master_password)
    users[username] = {'password': hashed_password}

def login_user(username, master_password):
    if username in users and check_password_hash(users[username]['password'], master_password):
        return True
    else:
        return False
