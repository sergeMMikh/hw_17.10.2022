# Create your tests here.


# class TestSomeCase(TestCase):
#     def test_my_view(self):
#         client = Client()
#         response = client.get('/test/')
#         self.assertEqual(response.content.decode(), "Test done!")

import pytest

from logistic.models import Product


@pytest.mark.django_db  # give test access to database
def test_product_create():
    # Create dummy data
    product = Product.objects.create(
        title="new product",
        description="The rely new product for test", )
    # Assert the dummy data saved as expected
    assert product.title == "new product"
    assert product.description == "The rely new product for test"
