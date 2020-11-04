from datetime import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post
from blog.models import Coach


class BlogTests(TestCase):

    def setUp(self):
        coach = Coach.objects.create(first_name='Coach', last_name='Ro', slug='coach-ro', blurb='this is some blurb')
        self.user = get_user_model().objects.create_user(
            username='testuser99',
            email='test@email.com',
            password='ThisisasEcReT'
        )

        self.post = Post.objects.create(
            title='This is a test post',
            text='This is some body text for this post',
            author=coach,
            slug='this-is-a-test-post',
            status='published',
            created=datetime(2020, 1, 1),
            publish=datetime(2020, 1, 2),
        )

    def test_repr(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_blog_post(self):
        self.assertEqual(f'{self.post.title}', 'This is a test post')
        self.assertEqual(f'{self.post.text}', 'This is some body text for this post')
        self.assertEqual(f'{self.post.status}', 'published')

    def test_blog_list(self):
        response = self.client.get(reverse('blog:blog-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the coach's plan blog")
        self.assertTemplateUsed(response, 'blog-list.html')

    def test_blog_detail(self):
        response = self.client.get('/blog/this-is-a-test-post/')
        no_response = self.client.get('/blog/not-a-valid-post/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'This is a test post')
        self.assertTemplateUsed(response, 'blog-detail.html')
