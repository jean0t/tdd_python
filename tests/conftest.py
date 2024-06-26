import asyncio
import pytest
from store.db.mongo import db_client
from store.core.schemas.product import ProductIn

@pytest.fixture(scope="session")
def event_loop():
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()

@pytest.fixture
def mongo_client():
	return db_client.get()


@pytest.fixture(autouse = True)
def clear_collections():
	yield
	collections_name = await mongo_client.get_database().list_collection_names()
	for collection_name in collections_name:
		if collection_name.startswith("system"):
			continue

		await mongo_client.get_database()[collection_name].delete_many({})

@pytest.fixture
def product_id():
	pass

@pytest.fixture
def product_in():
	ProductIn(**product_data())