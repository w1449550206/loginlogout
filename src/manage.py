#!/usr/bin/env python3


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from app import db
from app import User

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def init_data():
    tom = User(username='tom',  age=30, password='73453458')
    bob = User(username='bob', age=27, password='65757567567')
    lucy = User(username='lucy', age=24, password='gsfdgsfdgsdg')
    lily = User(username='lily',age=26, password='gfjhfgjgfj')
    alex = User(username='alex', age=91, password='575457567')
    john = User(username='john', age=29, password='hhjfhgjfghjfg')
    jack = User(username='jack', age=23, password='56345425232')
    tomas = User(username='tomas', age=18, password='985676345325')
    eva = User(username='eva',  age=21, password='ttrtryertthteh')
    ella = User(username='ella', age=23, password='hgfdsfghdhfhgfh')

    db.session.add_all([tom, bob, lucy, lily, alex, john, jack, tomas, eva, ella])
    db.session.commit()


if __name__ == '__main__':
    manager.run()
