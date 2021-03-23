from app.handler.index import (index, login, 
                               register, room_list, 
                               to_room, logout, 
                               create_room, my_rooms)
from app import socket_io

def register_rule(app):
    app.add_url_rule("/", "index", index, methods=["GET"])
    app.add_url_rule("/login", "login", login, methods=["POST", "GET"])
    app.add_url_rule("/register", "register", register, methods=["POST", "GET"])
    app.add_url_rule("/room_list", "rooms_list", room_list, methods=["GET"])
    app.add_url_rule("/room/<room_id>", "to_room", to_room, methods=["GET"])
    app.add_url_rule("/logout", "logout", logout, methods=["GET"])
    app.add_url_rule("/create_room", "create_room", create_room, methods=["POST"])
    # app.add_url_rule("/close_room", "close_room", close, methods=["GET"] )
    app.add_url_rule("/my_rooms", "my_rooms", my_rooms, methods=["GET"])
    
    