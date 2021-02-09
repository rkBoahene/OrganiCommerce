from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='python', slug='python')

    def test_category_model_entry(self):
        """
        Test Category model data insert/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        data = self.data1
        self.assertEqual(str(data), 'python')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, title='dj beginners', created_by_id=1, slug='dj-beginners', price='15.00', image='django')

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'dj beginners')
