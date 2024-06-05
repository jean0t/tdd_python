from store.core.schemas.product import ProductIn
from uuid import UUID

def test_schemas_validated_success():
	product = ProductIn(name="Notebook Lenovo", quantity=5, price=4000, status=True)
	assert product.name == "Notebook Lenovo"
	assert isinstance(product.id, UUID)
