from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    ''' Test the home page '''
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200) 

class ContactpageTests(SimpleTestCase):
    ''' Test the contact page '''
    def test_contactpage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_contactpage_url_name(self):
        response = self.client.get(reverse('pages:contact'))
        self.assertEqual(response.status_code, 200)


class SignuppageTests(TestCase):
    ''' Test the signup page '''
    email = 'rontest@blah.com'
    username = 'rontest'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                        [0].email, self.email)
