from flask.ext.script import Manager
from app import create_app

manager = Manager(create_app)


@manager.command
@manager.option('-e', '--env', dest='env', help='environment like dev, deploy to loading from settings')
def create_db(env='deploy'):
    """
    Create db using SQLAlchemy
    """
    machine = create_app(env)
    db = machine.config['db.machine']
    db.create_all()


@manager.command
@manager.option('-e', '--env', dest='env', help='environment like dev, deploy to loading from settings')
def drop_db(env='deploy'):
    """
    Drop db using SQLAlchemy
    """
    create_app(env)
    from app import db
    db.drop_all()


@manager.command
@manager.option('-e', '--env', dest='env', help='environment like dev, deploy to loading from settings')
def refresh_db(env='deploy'):
    """
    Refresh db using SQLAlchemy
    """
    create_app(env)
    from app import db
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()