from sqlalchemy.sql import func
from app import db, ma
from utils.base_model import BaseModel
from utils.to_password import to_password

class Users(db.Model, BaseModel):
    """
        用户信息表
    """
    __tablename__ = "users"
    union_id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
    username = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(50), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False)
    sid = db.Column(db.VARCHAR(100), comment="websocket sid")
    create_at = db.Column(db.DateTime, server_default=func.now())
    update_at = db.Column(db.DateTime)
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = to_password(password)
        self.email = email
        

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Users
        fields = ("union_id", "username", "password", "email", "sid", "create_at", "update_at")
        