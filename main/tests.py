from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_news_creation(self):
        news = Product.objects.create(
          title="BURHAN FC WINS",
          content="BURHAN FC 1-0 PANDA BC",
          category="match",
          news_views=1001,
          is_featured=True
        )
        self.assertTrue(news.is_product_hot)
        self.assertEqual(news.category, "match")
        self.assertTrue(news.is_featured)
        
    def test_news_default_values(self):
        news = Product.objects.create(
          title="Test News",
          content="Test content"
        )
        self.assertEqual(news.category, "update")
        self.assertEqual(news.product_views, 0)
        self.assertFalse(news.is_featured)
        self.assertFalse(news.is_product_hot)

    def test_increment_views(self):
        news = Product.objects.create(
          title="Test News",
          content="Test content"
        )
        initial_views = news.product_views
        news.increment_views()
        self.assertEqual(news.product_views, initial_views + 1)

    def test_is_product_hot_threshold(self):
        # Test product with exactly 20 views (should not be hot)
        product_20 = Product.objects.create(
          title="Product with 20 views",
          content="Test content",
          product_views=20
        )
        self.assertFalse(product_20.is_product_hot)

        # Test product with 21 views (should be hot)
        product_21 = Product.objects.create(
          title="Product with 21 views",
          content="Test content",
          product_views=21
        )
        self.assertTrue(product_21.is_product_hot)