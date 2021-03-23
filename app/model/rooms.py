from sqlalchemy.sql import func
from app import db, ma
from utils.base_model import BaseModel
from app.model.users import UserSchema


class Rooms(db.Model, BaseModel):
    """
        聊天室表
    """
    __tablename__ = "chat_room"
    
    union_id =  db.Column(db.BigInteger, autoincrement=True, primary_key=True, comment="聊天室id")
    room_name = db.Column(db.VARCHAR(20), unique=True, comment="聊天室名字")
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.union_id", ondelete="CASCADE"),comment="房间主人id")
    describe = db.Column(db.VARCHAR(500), comment="房间简介")
    number = db.Column(db.VARCHAR(7), unique=True, comment="房间编号, 1356879")
    room_status = db.Column(db.SmallInteger, default=1, comment="房间状态,0 未开始，1已开始")
    create_at = db.Column(db.DateTime, server_default=func.now())
    update_at = db.Column(db.DateTime)
    user = db.relationship("Users", backref=db.backref("chat_room"))
    
    def __init__(self, room_name, user_id, describe, number, room_status):
        self.room_name = room_name
        self.user_id = user_id
        self.describe = describe
        self.number = number
        self.room_status

class RoomsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Rooms
        fields = ("union_id", "room_name", "user_id", "describe",\
            "number", "room_status", "create_at", "update_at", "user")
    
    user = ma.Nested(UserSchema, only=["union_id", "username"])
    
    