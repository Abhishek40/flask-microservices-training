from werkzeug.exceptions import HTTPException

class ProductNotFound(HTTPException):
    def __init__(self, message="Product not found", code=404):
        self.message = message
        self.code = code
        super().__init__()

class InvalidProductPayload(HTTPException):
    def __init__(self, message="Product payload has invalid input", code=400):
        self.message = message
        self.code = code
        super().__init__()

class ProductExistsException(HTTPException):
    def __init__(self, message="Product already exists", code=400):
        self.message = message
        self.code = code
        super().__init__()