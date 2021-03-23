from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import weChat, db

public_app = weChat()

migrate = Migrate(public_app, db)
manager = Manager(public_app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()