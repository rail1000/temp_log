from flask import Flask, Blueprint
from App.views import blue
from App.views1 import blue as blue1


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'

app.register_blueprint(blueprint=blue)
app.register_blueprint(blueprint=blue1)



if __name__ == '__main__':
    app.run(debug=True)
