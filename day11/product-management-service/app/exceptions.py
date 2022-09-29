from werkzeug.exceptions import HTTPException

class ProductNotFound(HTTPException):
    def __init__(self, message="Product not found", code=404):
        self.message = message
        self.code = code
        super().__init__()