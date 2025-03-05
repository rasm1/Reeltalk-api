from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='Nick', password='123')

    def test_can_list_posts(self):
        Nick = User.objects.get(username='Nick')
        Post.objects.create(owner=Nick, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='Nick', password='123')
        response = self.client.post('/posts/', {'title': 'a title', 'movie_title': "kungfu panda"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title', 'movie_title': "Shrek"})
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)