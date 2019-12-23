#!/usr/bin/env python3

import os

import pymysql
from flask import Flask
from flask import abort
from flask import request
from flask import session
from flask import render_template
from flask import redirect
from flask import make_response
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = 'M\xd2\x16\xa0K\x01\x0f@\x9f(\xab2V\xd7\xe3\x00'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vicky:wangwenqi5261@localhost/loginlogout'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(32), nullable=False)
    age = db.Column(db.Integer, default=18)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 获取参数
        username = request.form.get('username')
        password = request.form.get('password')

        # 验证用户名和密码
        user = User.query.filter_by(username=username, password=password).first()
        print(user)

        if user is None:
            return redirect('/login')
        else:
            session['uid'] = user.id  # 将用户 ID 记录到 session 中
            return redirect('/show')
    else:
        return render_template('login.html')


@app.route('/show')
def show():
    '''展示用户信息'''
    uid = session.get('uid')  # 从 Session 中获取用户 ID
    if uid is None:
        abort(403)
    else:
        user = User.query.get(uid)
        return render_template('show.html', user=user)


@app.route('/logout')
def logout():
    session.pop('uid')
    return redirect('/login')


if __name__ == '__main__':
    app.debug = True
    app.run()
