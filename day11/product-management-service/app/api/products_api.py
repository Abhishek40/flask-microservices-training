from flask import request
from flask_restful import Resource
from ..models.product import Product
from ..schemas.product_schema import ProductSchema
from ..exceptions import ProductExistsException,InvalidProductPayload, ProductNotFound
from app import restful_api, db, app
from ..utils import create_demo_product

product_schema = ProductSchema()

class ProductsApi(Resource):

    def get(self):
        return [product.to_json() for product in Product.query.all()]

    def post(self):
        errors = product_schema.validate(request.json)
        if errors:
            raise InvalidProductPayload
        existing_product = Product.query.filter_by(name=request.json.get('name')).first()
        if (existing_product is not None):
            raise ProductExistsException(f'Product [{existing_product.name}] already exists"')
        product = Product.from_json(request.json)
        db.session.add(product)
        db.session.commit()
        new_product = Product.query.filter_by(name=product.name).first()
        return new_product.to_json(), 201
    
    def put(self):
        return {'message': 'Hello PUT'}

    def delete(self):
        return {'message': 'All users are safe from delete'}

restful_api.add_resource(ProductsApi, '/api/products')

@app.before_first_request

def before_first_request():
    print("before_first_request")
    product1 = Product.from_json({
        'name': 'Book1',
        'description': 'Book to be read',
        'price': 20,
        'currency': '₹',
        'stock': 20,
        'active': True
        })  
    create_demo_product(db, product1)