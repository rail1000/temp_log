from flask import Blueprint, request,render_template
from App.model1 import model1
from App.views import blue

blue=Blueprint("sec_blue",__name__)


@blue.route('/query/<family>',methods=['GET','POST'])
def query(family):
    query_fam = model1(family,'','','')
    artic =query_fam.query_family()
    return render_template('all_family.html',artic=artic)


@blue.route('/artic/<id>',methods=['GET','POST'])
def artic(id):
    query_no = model1('','','',id)
    artic = query_no.query_id()
    return render_template('artic_title.html',artic=artic)

@blue.route('/querytitle/',methods=['GET','POST'])
def query_title():
    key_word = request.form.get('key_word')
    query_k = model1('', key_word ,'','')
    artic = query_k.query_title()

    return render_template('all_family.html',artic=artic)