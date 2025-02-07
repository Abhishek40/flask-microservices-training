from locale import currency
from wsgiref import validate
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range, OneOf


class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=Length(max=30))
    description = fields.Str(required=False, validate=Range(min=20, max=300))
    price = fields.Int(required=True, validate=Range(min=1, max=99999))
    currency = fields.Str(required=True, validate=OneOf(['₹','$', '€']))
    stock = fields.Int(required=True, validate=Range(min=1, max=999))
    active = fields.Bool(required=True)