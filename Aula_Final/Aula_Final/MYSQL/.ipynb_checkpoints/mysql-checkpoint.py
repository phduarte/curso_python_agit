from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class Test(db.Model): # test eh o nome da tabela
                      # db.Model traz (herda) as funcionalidades do SQLAlchemy(app)
    id = db.Column(db.Integer, primary_key=True)

class Member(db.Model):

    # nao eh necessario o __init__ pois ele ja herdou de db.Model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))
    join_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Member %r>' % self.username


if __name__ == '__main__':
    app.run()