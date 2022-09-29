from .models.product import Product

def create_demo_product(db, product):
		existing_product = Product.query.filter_by(name=product.name).first()
		if existing_product is not None:
			print(f"First product [{existing_product.name}] already exits. Skipping creation on startup")
			return
		#user.password = flask_bcrypt.generate_password_hash(user.password).decode('utf-8')
		db.session.add(product)
		db.session.commit()
		print(f"Successfully Created initial demo product [{product.name}]")