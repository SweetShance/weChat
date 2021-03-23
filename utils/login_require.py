from flask import request, render_template, session

def login_require(func):
    def wrapper(*args, **kwargs):
        cookie_uuid = request.cookies.get("user_about")
        if not cookie_uuid: 
            return render_template("index.html")
        else:
            user_about = session.get(cookie_uuid)
            if not user_about:
                return render_template("index.html")
            return func(*args, **kwargs)
    return wrapper