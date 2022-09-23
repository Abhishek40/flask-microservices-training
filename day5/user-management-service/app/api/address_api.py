from flask import request
from flask_restful import Resource
from ..database import get_db_connection, close_db_connection, commit_and_close_db_connection
from ..database import address_db
from ..models.address import Address


class AddressApi(Resource):

    def get(self, id):
        conn = get_db_connection()
        user_address = address_db.get_address_details(conn, id)
        close_db_connection(conn)
        return user_address

    def put(self, id):
        conn = get_db_connection()
        address_db.get_address_details(conn, id)
        address_db.update_address_details(conn, id, Address.from_json(request.json))
        user_address = address_db.get_address_details(conn, id)
        commit_and_close_db_connection()
        return user_address

    def delete(self, id):
        conn = get_db_connection()
        user_address = address_db.get_address_details(conn, id)
        address_db.delete_address(conn, id)
        commit_and_close_db_connection()
        return {'message': f'Address [{user_address["address_line_1"]}] deleted from the database'}