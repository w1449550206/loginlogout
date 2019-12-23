#!/usr/bin/env python3

import os

import pymysql
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

# 项目文件夹的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vicky:wangwenqi5261@localhost/loginlogout'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index = True)
    password = db.Column(db.String(32),nullable=False)
    age = db.Column(db.Integer, default=18)


@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        # # uid = int(request.form['uid'])
        # # user = Student.query.get(uid)
        # # user.gender = request.form['gender']
        # # user.chinese = int(request.form['chinese'])
        # # user.math = int(request.form['math'])
        # # db.session.add(user)
        # # db.session.commit()
        # return redirect('/')
        pass
    else:
        # uid = int(request.args['uid'])
        # user = Student.query.get(uid)
        return render_template('login.html')


@app.route('/show')
def show():
    # uid = int(request.args['uid'])
    # user = Student.query.get(uid)
    # return render_template('info.html', user=user)
    pass



if __name__ == '__main__':
    app.debug = True
    app.run()
