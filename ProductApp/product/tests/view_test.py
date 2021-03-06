import json

from unittest import TestCase
from django.test import Client

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .model_test import BaseTestClass


class IndexViewTest(BaseTestClass):

    def setUp(self):
        self.client = Client()
    
    def test_render_welcome_page(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Products')
    

class ProductRecordViewTest(BaseTestClass):

    def test_render_welcome_page(self):
        self.client = Client()
        response = self.client.get(reverse('product_record'))
        
        json_content = json.loads(response.content)

        self.assertEqual( json_content['products_info'][0]['symbol'], 'TKC^17^18')
        self.assertEqual(json_content['message'], 'all products record')


class ProductPlacedOrderViewTest(BaseTestClass):

    def test_render_placed_order_page(self):
        client = Client()
        client.login(username='testuser', password='testuser123')
        response = client.get(reverse('all_place_order'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Place Orders')


class SearchProjectTestCases(BaseTestClass):

    def test_search_product_test(self):
        self.client = Client()
        response = self.client.get('/products/search-product/?q=TKC')
        
        json_content = json.loads(response.content)

        self.assertEqual( json_content['products_info'][0]['symbol'], 'TKC^17^18')
        self.assertEqual(json_content['message'], 'search products record')
