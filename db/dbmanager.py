import torndb
from config import db_host, db_name, db_password, db_user

db = torndb.Connection(db_host, db_name, db_user, db_password)
db.execute("set names utf8")
db.execute("set session time_zone = '+8:00'")