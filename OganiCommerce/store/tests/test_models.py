from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='test_cat', slug='test_slug')

    def test_category_model_entry(self):
        """
        Test category model data insertion/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'test_cat')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='test_cat', slug='test_slug')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, name='test', created_by_id=1, slug='test', price='5.0', image='test')

    def test_products_model_entry(self):
        """
        Test product model default insert/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'test')
