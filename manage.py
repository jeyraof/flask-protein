from flask.ext.script import Manager
from app import create_app

manager = Manager(create_app)


@manager.command
def database(create=False, drop=False):
    """
    Managing database using SQLAlchemy
    """
    from app import db
    actions = {
        (True, False): (lambda x: [x.create_all])(db),
        (False, True): (lambda x: [x.drop_all])(db),
    }.get((True if create else False, True if drop else False), [])

    if actions:
        for action in actions:
            action()

    else:
        print u'usage: python manage.py database {--create, --drop}'


if __name__ == '__main__':
    manager.add_option("-s", "--setting", dest="setting", required=False, default='dev')
    manager.run()