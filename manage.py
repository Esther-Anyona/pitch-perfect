from app import create_app, db
from app.models import User, Pitch
from flask_script import Manager, Server

app = create_app('development')

manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch=Pitch )

if __name__ == '__main__':
    manager.run()