from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://homestead:secret@localhost/appku?host=localhost?port=3306'
db = SQLAlchemy(app)
ma = Marshmallow(app)

from Products import *
from Categorys import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')