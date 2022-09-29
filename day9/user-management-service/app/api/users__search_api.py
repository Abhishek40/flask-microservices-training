from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from ..models.user import User
from ..database import get_db_connection, close_db_connection, commit_and_close_db_connection
from ..database import user_db
from ..schemas.user_schema import UserSchema
from ..exceptions import InvalidUserPayload, UserExistsException
from app import restful_api, flask_bcrypt
from ..decorators.security import admin_required

class UsersSearchApi(Resource):
	decorators = [jwt_required(optional= True)]	#Add appropriate decorators
	def get(self, email):
		if(email != None):
			conn = get_db_connection()
			user = user_db.get_user_details_from_email(conn, email)
			close_db_connection(conn)
			return user.to_json()
		else:
			return 'not authenticated user'
restful_api.add_resource(UsersSearchApi, '/api/users/<string:email>')
		#pass #Add logic to give full user details if accesed by a user with valid token else return just name and email

# Uncomment the below line by adding a valid url mapping for the user search API
#restful_api.add_resource(UsersSearchApi, '<valid-mapping>')