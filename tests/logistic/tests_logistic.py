import pytest

from logistic.models import Product


@pytest.mark.django_db
def test_product_create():
    # Create dummy data
    product = Product.objects.create(title="new product", description="The rely new product for test", )
    # # Assert the dummy data saved as expected
    assert product.title == "new product"
    assert product.description == "The rely new product for test"

    # assert 2 == 2
