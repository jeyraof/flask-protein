from flask.ext.script import Manager
from app import create_app

if __name__ == '__main__':
    machine = create_app()