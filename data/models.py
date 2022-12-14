import data.database as db
import hashlib


def get_user(email):
    cursor = db.main_db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE email='{email}' ")
    record = cursor.fetchone()
    print(record[0])


def is_authenticated(email, password):
    password = hashlib.md5(password.encode()).hexdigest()
    cursor = db.main_db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE email='{email}' and password='{password}' ")
    user = cursor.fetchone()
    user_id = user[0]
    return user_id

