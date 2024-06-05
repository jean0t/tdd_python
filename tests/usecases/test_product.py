from store.usecases.product import ProductUsecase

async def test_usecases_should_return_success():
	result = await ProductUsecase.create(body=product_data())

	assert isinstance(result, ProductOut)
