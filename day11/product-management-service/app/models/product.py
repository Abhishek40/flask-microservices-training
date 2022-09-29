from app import db
class Product(db.Model):
    __tablename__ = 'UMS_PRODUCT_LIST'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(300))
    price = db.Column(db.Integer(99999))
    currency = db.Column(db.String(10))
    stock = db.Column(db.Integer(999))
    active = db.Column(db.Boolean())

    def __init__(self, name, description, price, currency, stock, active):
        self.name = name
        self.description = description
        self.price = price
        self.currency = currency
        self.stock = stock
        self.active = active
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'currency': self.currency,
            'stock': self.stock,
            'active': self.active
        }

    @staticmethod
    def from_json(json_dct):
        return Product(json_dct['name'],
                        json_dct['description'],
                        json_dct['price'],
                        json_dct['currency'],
                        json_dct['stock'],
                        json_dct['active']
                        )

