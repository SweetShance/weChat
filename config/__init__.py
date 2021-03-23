import datetime

# mysql

DIALECT = "mysql"
DRIVER = "pymysql"
HOST = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "295213"
DATABASE = "weChat"

SQLALCHEMY_DATABASE_URI = f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 60

TEMPLATE_FOLDER = "templates"
SECRET_KEY = "123456"
# PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)