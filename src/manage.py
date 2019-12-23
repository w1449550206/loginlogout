#!/usr/bin/env python3


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from app import db
from app import Student

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# @manager.command
# def init_db():
#     db.create_all()


@manager.command
def init_data():
    tom = Student(name='tom', gender='male', chinese=90, math=78)
    bob = Student(name='bob', gender='male', chinese=87, math=65)
    lucy = Student(name='lucy', gender='female', chinese=74, math=73)
    lily = Student(name='lily', gender='female', chinese=86, math=90)
    alex = Student(name='alex', gender='male', chinese=91, math=77)
    john = Student(name='john', gender='male', chinese=79, math=72)
    jack = Student(name='jack', gender='male', chinese=60, math=99)
    tomas = Student(name='tomas', gender='male', chinese=88, math=98)
    eva = Student(name='eva', gender='female', chinese=100, math=85)
    ella = Student(name='ella', gender='female', chinese=70, math=81)

    db.session.add_all([tom, bob, lucy, lily, alex, john, jack, tomas, eva, ella])
    db.session.commit()


if __name__ == '__main__':
    manager.run()
