from django.test import TestCase, Client


# from logistic.models import Product


class TestLogic(TestCase):
    # def test_view(self):
    #     client = Client()
    #     response = client.get('/test/')
    #     self.assertEqual(response.content.decode(), "Test done!")

    def test_2_2(self):
        self.assertEqual(2, 2)
