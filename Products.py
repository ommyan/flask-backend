from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app import *

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(80))
    type_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    def __init__(self, id,nama, type_id,category_id):
        self.id = id
        self.nama = nama
        self.type_id = type_id
        self.category_id = category_id

class ProductsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','nama', 'type_id','category_id')


product_schema = ProductsSchema()
product_schema = ProductsSchema(many=True)


# endpoint to show all users
@app.route("/product", methods=["GET"])
def products():
    all_products = Products.query.all()
    result = product_schema.dump(all_products)
    return jsonify(result.data)

@app.route("/product", methods=["POST"])
def add_product():
    nama = request.json['nama']
    type_id = request.json['type_id']
    category_id = request.json['category_id']
    new_product = Products(nama=nama, type_id=type_id,category_id=category_id)

    db.session.add(new_product)
    db.session.commit()

    return "Sukses"