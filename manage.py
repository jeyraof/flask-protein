from flask.ext.script import Manager
from app import create_app

manager = Manager(create_app)
manager.add_option('-e', '--env', dest='env', required=False)

if __name__ == '__main__':
    manager.run()