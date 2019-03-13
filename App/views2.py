from flask import Blueprint, request, render_template, session
from App.model2 import model2
from App.model3_add_artic import model3

blue=Blueprint("third_blue",__name__)

@blue.route('/user/',methods=['GET','POST'])
def user():

    username = session.get('user')
    no = model2(username)

    artic = no.query_artic()

    return render_template("user.html",artic=artic)


@blue.route('/addartic/',methods=['GET','POST'])
def add_artic():
    username = session.get('user')
    title = request.form.get('title')
    content = request.form.get('content')
    family = request.form.get('family')

    now = model3(title,content,family,username)
    now.insert_artic()
    no = model2(username)

    artic = no.query_artic()

    return render_template('user.html',artic=artic)


@blue.route('/tans/',methods=['GET','POST'])
def tans():

    return render_template('add_artic.html')


