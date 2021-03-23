import json
from flask import request, session
from flask_socketio import join_room, rooms, close_room
from app.model.users import Users
from app import socket_io
from app.model.rooms import Rooms
from utils.login_require import login_require


"""
world 是聊天大厅的socket 接口

rooms 是房间的接口
"""

@socket_io.on("connect", namespace="/world")
def connect_socket():
    """
        进来后我们将当前连接的 sid 记录到数据库,
        msg 格式为json的
    """
    # 获取sid
    user_sid = request.sid
    # 获取cookie 中用户uuid 标识
    cookie_uuid = request.cookies.get("user_about")
    if not cookie_uuid:
        socket_io.emit("connect", "登录信息有误请重新登录", namespace="/world")
        return 
    user_about = session.get(cookie_uuid)
    if not user_about:
        socket_io.emit("connect", "登录信息有误请重新登录", namespace="/world")
        return 

    # 获取用户的union_id
    user_union_id = user_about.get("union_id")
    user = Users.query.get_or_404(user_union_id)
    user.sid = user_sid
    user.update()
    socket_io.emit("connect", "连接成功", namespace="/world")
    

@socket_io.on("message", namespace="/world")
def world_socket(msg):
    # 分发消息，只是不发给
    cookie_uuid = request.cookies.get("user_about")
    if not cookie_uuid: 
        return render_template("index.html")
    data = session.get(cookie_uuid)
    data["user_uuid"] = cookie_uuid
    data["text"] = msg
    socket_io.emit("message", data, namespace="/world")
    

@socket_io.on("join", namespace="/room")
def on_join(data):
    cookie_uuid = request.cookies.get("user_about")
    user_data = session.get(cookie_uuid)

    username = user_data['username']
    room_id = data['room_id']
    
    room = Rooms.query.get_or_404(room_id)
    room_name = room.room_name
    join_room(room_name)
    # # socket_io.emit('message', user_data)
    socket_io.emit("status", {"room": room_name, "text":f"{username}加入房间{room.room_name}"}, namespace="/room", room=room_name)


@socket_io.on("room", namespace="/room")
def world_socket(msg):
    # 分发消息，只是不发给
    cookie_uuid = request.cookies.get("user_about")
    if not cookie_uuid: 
        return render_template("index.html")
    data = session.get(cookie_uuid)
    data["user_uuid"] = cookie_uuid
    data["text"] = msg["text"]
    room_name = msg["room_name"]
    socket_io.emit("message", data, namespace="/room", room=room_name)


@socket_io.on("close room", namespace="/room")
def close(data):
    room_id = data.get("room_id")
    room = Rooms.query.get_or_404(room_id)
    room.room_status = 0
    room.update()
    socket_io.emit("close_status", "该房间已关闭", namespace="/room", room=room.room_name)
    close_room(room.room_name)
    
    