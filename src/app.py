#!/usr/bin/env python3

import os

import pymysql
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import make_response
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
        # 获取参数
        username=request.form.get('username')
        password=request.form.get('password')

        # 验证用户名和密码
        user = User.query.filter_by(username=username,password=password).first()

        if user is None:
            return redirect('/login')
        else:
           
            # 进行模板渲染
            html = render_template('show.html',user=user)
            response = make_response(html)

            #通过cookie记录登陆过的用户id
            response.set_cookie('uid',user.id)
            return render_template('show.html',user-user)
        
    else:
        return render_template('login.html')


@app.route('/show')
def show():
    #展示用户信息,从cookie里获取用户id
    uid = request.cookies.get('uid')
    if uid is None:
        return redirect('/login')
    else:
        user = User.query.get(uid)
        return render_template('show.html', user=user)
   



if __name__ == '__main__':
    app.debug = True
    app.run()
