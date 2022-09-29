from flask import request
from flask_restful import Resource
from ..models.product import Product
from app.exceptions import ProductNotFound, InvalidProductPayload
from ..schemas.product_schema import ProductSchema
from app import restful_api, db

product_schema = ProductSchema()

class ProductApi(Resource):

    def get(self, id):
        product = Product.query.get(id)
        if not product:
            raise ProductNotFound(f'Product with ID [{id}] not found')
        return product.to_json()

    def put(self, id):
        product = Product.query.get(id)
        if not product:
            raise ProductNotFound(f'Product with ID [{id}] not found')
        errors = product_schema.validate(request.json)
        if errors:
            raise InvalidProductPayload(errors, 400)
        updated_product = Product.from_json(request.json)
        product.name = updated_product.name
        product.description = updated_product.description
        product.price = updated_product.price
        product.currency = updated_product.currency
        product.stock = updated_product.stock
        product.active = updated_product.active
        db.session.commit()
        return product.to_json()

    def delete(self, id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return {'message': f'Product [{product.name}] deleted from database'}

restful_api.add_resource(ProductApi, '/api/products/<int:id>')
