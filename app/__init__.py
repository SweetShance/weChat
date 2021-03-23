from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
import logging
import config

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
socket_io = SocketIO()

logger = logging.getLogger("gunicorn.ifo")
handler = logging.FileHandler("error.log", encoding="utf-8")
logging_format = logging.Formatter('%(asctime)s - %(levelname)s \
                                    - %(filename)s - %(funcName)s \
                                    - %(lineno)s - %(message)s')
# logger.addHandler(handler)
logger.setLevel(logging.INFO)

def weChat():
    app = Flask(__name__)
    app.config.from_object(config)
    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    from app.routes.register import register_rule
    register_rule(app)
    socket_io.init_app(app, cors_allowed_origins="*")
    # 导入socketio 视图
    from app.handler import socket_handler
    
    return app


if __name__ == "__main__":
    socket_io.run(weChat, debug=True, host="127.0.0.1", port=80)