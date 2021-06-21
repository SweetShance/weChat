通过socket通讯实现了一个简单的大厅聊天和开房间聊天
flask_socketio 文档
https://flask-socketio.readthedocs.io/en/latest/

socketio 文档
https://socketio.bootcss.com/#examples

环境： flask + flask_socketio + mysql 

运行： 

  1.先创建数据库名 weChat， 或者根据内容修改 config/__init__.py 的数据库配置

2. pip install -r requirement.txt  配置环境

3. 在weChat 目录下执行

   ```bash
   python manage.py migrate # 数据库迁移
   python manage.py upgrade 
   
   set flask_app=app:weChat
   set flask_env=development
   flask run
   ```

   进入网页：http://127.0.0.1:5000 即可

   

