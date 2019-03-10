# -*- coding: UTF-8 -*-

from flask import app, Blueprint, url_for, render_template, Response, session
from flask import request
from App.models import  model
import pymysql


conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
blue = Blueprint("first_blue", __name__)

@blue.route('/create/',methods=['GET','POST'])
def create():
    create_DB()
    return  'successfully'



@blue.route('/reg/',methods=['GET','POST'])
def reg():
    return render_template("regst.html")


@blue.route('/regst/',methods=['GET','POST'])
def regist():
    sql='123'
    if request.method == 'GET':
        return render_template("regst.html")
    username = request.form.get('username')
    password = request.form.get('password')
    password1 = request.form.get('password1')
    email = request.form.get('email')

    if request.method == "POST":
        if password == password1:
            new = model(username, password, email)
            new.regist()
            return 'successfully'
        return 'filed'
    return 'filed1'

@blue.route('/insert/',methods=['GET','POST'])
def insert():
    regist()
    return 'successfully'

@blue.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        new = model(username,password,email)
        rl_password=new.log()
        if str(rl_password) == password:

            session['user']=username
            return render_template('home.html')
        else :
            return 'filed2'+str(rl_password)
    elif request.method == "GET":
        return render_template('login.html')


@blue.route('/home/')
def home():

    username=session.get('user')
    return render_template('home.html', username=username)
