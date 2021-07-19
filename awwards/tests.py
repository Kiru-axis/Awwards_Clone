from django.test import TestCase
from .models import *
# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Test', password='test')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Test')
        self.post = Post.objects.create(id=1, title='Post', photo='https://cutt.ly/UmBUMAX', description='desc',
                                        user=self.user, url='http://google.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))
