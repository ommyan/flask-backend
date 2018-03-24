from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app import *

''' 
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://homestead:secret@localhost/appku?host=localhost?port=3306'
db = SQLAlchemy(app)
ma = Marshmallow(app) '''

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))
    def __init__(self, category ):
        self.nama = category

class CategorySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','category')

category_schema = CategorySchema()
category_schema = CategorySchema(many=True)


# endpoint to show all users
@app.route("/category", methods=["GET"])
def category():
    all_cat = Category.query.all()
    result = category_schema.dump(all_cat)
    return jsonify(result.data)
