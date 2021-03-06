from app import create_app,db
from flask_script import Manager,Server
import manage
from app.models import User,Comment,Pitch,Category
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

#Migration

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Comment = Comment, Pitch= Pitch, Category = Category )
if __name__ == '__main__':
    manager.run()