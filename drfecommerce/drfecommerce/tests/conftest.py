import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import ( 
    CategoryFactory,
    ProductFactory,
    ProductImageFactory,
    ProductLineFactory,
)
# AttributeFactory,; AttributeValueFactory,; ProductTypeFactory,

register(CategoryFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
# register(AttributeValueFactory)
# register(AttributeFactory)
# register(ProductTypeFactory)


@pytest.fixture
def api_client():
    return APIClient
