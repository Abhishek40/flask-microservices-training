from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..schemas.address_schema import AddressSchema
from ..exceptions import InvalidAddressPayload
from ..models.address import Address
from app import restful_api, db
from ..decorators.security import admin_or_self_required

address_schema = AddressSchema()

class AddressApi(Resource):
	decorators = [jwt_required(), admin_or_self_required(user_id_param='user_id')]
	def get(self, user_id):
		user_address = Address.query.filter_by(user_id=user_id)
		return [address.to_json() for address in user_address]

	def put(self, user_id):
		Address.query,filter_by(user_id=user_id)
		new_address = Address.from_json(request.json)
		new_address.user_id = user_id
		db.session.add(new_address)
		db.session.commit()
		user_address = Address.query.filter_by(user_id=user_id)
		return [address.to_json() for address in user_address],201

	def delete(self, user_id):		
		user_address = Address.query.filter_by(user_id=user_id)
		db.session.delete(user_address)
		db.session.commit()
		return {'message': f'User address[{user_address.address}] deleted from DB'}


restful_api.add_resource(AddressApi, '/api/user/<int:user_id>/address')