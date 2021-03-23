import json
from uuid import uuid4
from flask import request, redirect, render_template, jsonify, make_response, session, url_for
from app.model.users import Users, UserSchema
from app.model.rooms import Rooms, RoomsSchema
from utils.to_password import to_password
from utils.login_require import login_require


user_schema = UserSchema()
rooms_schema_many = RoomsSchema(many=True)


@login_require
def index():
    cookie_uuid = request.cookies.get("user_about")
    user_about = session.get(cookie_uuid)
    user_uuid = user_about.get("union_id")
    user = Users.query.get_or_404(user_uuid)    
    return render_template("index.html", context=user_schema.dump(user))

def login():
    username = request.form.get("username")
    password = request.form.get("password")
    new_password = to_password(password)
    username_user = Users.query.filter_by(username=username, password=new_password)
    if username_user.count() <= 0:
        resp = make_response(redirect(request.host_url+"?error='用户名密码错误'"))
        resp.delete_cookie("user_about")
        return  resp    
    
    resp = make_response(redirect(url_for("index")))
    
    # 生成uuid
    cookie_uuid = uuid4().hex
    # 设置
    resp.set_cookie("user_about", cookie_uuid)
    resp.set_cookie("username", username_user.first().username)
    # 设置session
    session[cookie_uuid] = json.loads(user_schema.dumps(username_user.first()))
    return resp


def register():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    code = request.form.get("code")
    username_user_count = Users.query.filter_by(username=username).count()
    if username_user_count > 0:
        return redirect(request.host_url + "?error='该用户名已存在'")
    
    email_user_count = Users.query.filter_by(email=email).count()
    if email_user_count > 0:
        return redirect(request.host_url + "?error='该邮箱已经被注册'")
    
    # email_code =  session[email]
    # if email_code != code:
    #     return redirect(request.host_url + "?error='验证码不正确'")
    
    # 注册用户
    user = Users(username, password, email)
    user.create()
    resp = make_response(redirect(url_for("index")))
    # 生成uuid
    cookie_uuid = uuid4().hex
    # 设置
    resp.delete_cookie("user_about")
    resp.set_cookie("user_about", cookie_uuid)
    resp.set_cookie("username", user.username)
    # 设置session
    session[cookie_uuid] = json.loads(user_schema.dumps(user))
    return resp


def logout():
    cookie_uuid = request.cookies.get("user_about")
    session.pop(cookie_uuid)
    host_url = request.host_url
    res = make_response(redirect(host_url))
    res.delete_cookie("username")
    res.delete_cookie("user_about")
    return res
    
    

def room_list():
    page = int(request.args.get("page", "1"))
    # per_page = request.args.get("per_page", "35")
    
    rooms = Rooms.query.filter_by(room_status="1").paginate(
        page=page, per_page=35, error_out=True, max_per_page=None
    )
    if rooms:
        return make_response(jsonify({"status": True, "data": rooms_schema_many.dump(rooms.items)}))
    else:
        return make_response(jsonify({"status": False, "msg": "暂无房间"}))
    
    
def to_room(room_id):
    # 获取room 信息
    cookie_uuid = request.cookies.get("user_about")
    if not cookie_uuid: 
        return redirect(url_for("index"))
    else:
        user_about = session.get(cookie_uuid)
        user_uuid = user_about.get("union_id")
        user = Users.query.get_or_404(user_uuid)   
        room =  Rooms.query.filter_by(union_id=room_id).first()
        start = request.host_url.split("?")[-1]
        if start and user.union_id == room.user_id:
            room.room_status = 1
            room.update()
        
        if(room.room_status == 0):
            return redirect(url_for("index"))
        if room.user_id == user.union_id:
            context = {
                "my_room": True
            }
        else:
            context = {}
        
        return render_template("room.html", context=context)    

@login_require
def my_rooms():
    cookie_uuid = request.cookies.get("user_about")
    if not cookie_uuid: 
        return make_response(jsonify({"status": False, "msg": "暂未登录"}))
    else:
        user_about = session.get(cookie_uuid)
        user_uuid = user_about.get("union_id")
        rooms =  Rooms.query.filter_by(user_id=user_uuid)
        if(rooms.count() == 0):
            return make_response(jsonify({"status": False, "msg": "暂无房间"}))
        else:
            return make_response(jsonify({"status": True, "data": rooms_schema_many.dump(rooms)}))
        

@login_require
def create_room():
    room_name = request.form.get("room_name")
    room_number = request.form.get("room_number")
    room_describe = request.form.get("room_describe")
    # 获取用户信息，创建
    cookie_uuid = request.cookies.get("user_about")
    user_about = session.get(cookie_uuid)
    union_id = user_about.get("union_id")
    #  唯一性判断
    name_room_count = Rooms.query.filter_by(room_name=room_name).count()
    if name_room_count > 0:
         return redirect(request.host_url + "?error='该房间名已被注册'")
     
    number_room_count = Rooms.query.filter_by(number=room_number).count()
    print(number_room_count)
    if number_room_count > 0:
        return  redirect(request.host_url + "?error='该房间编号已被注册'")
     
    user_room_count = Rooms.query.filter_by(user_id=union_id).count()
    if user_room_count > 0:
        return redirect(request.host_url + "?error='一个人只能创建一个房间，您已经创建过房间了'")    
    # 创建
    room = Rooms(room_name=room_name, user_id=union_id, describe=room_name, number=room_number, room_status=1)
    room.create()
    return redirect(url_for("to_room", room_id=room.union_id))




