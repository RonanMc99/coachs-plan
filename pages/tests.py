from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):

    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200) 

class ContactpageTests(SimpleTestCase):

    def test_contactpage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contactpage_url_name(self):
        response = self.client.get(reverse('pages:contact'))
        self.assertEqual(response.status_code, 200) 