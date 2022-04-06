from django.test import TestCase
from .models import Article

# Create your tests here.

class ArticleTestCase(TestCase):
    def setup(self):
        Article.objects.create(
            title='tyu',
            content='tyu'
        )
    
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
    
    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), 1)