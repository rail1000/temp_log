from flask import Blueprint, url_for

from App.views import blue

blue=Blueprint("sec_blue",__name__)


@blue.route('/index/')
def index():
    result = url_for("first_blue.IN")
    return result
