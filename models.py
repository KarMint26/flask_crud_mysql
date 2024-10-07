from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Students('{self.name}', '{self.email}')"
    
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Teachers('{self.name}', '{self.email}')"
