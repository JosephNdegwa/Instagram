from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Following, Image

class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = User.objects.create(username="ken")
    
    def test_proxy_user(self):
        self.profile.bio = ""
        self.assertEqual(self.profile.bio, "")

class FollowingTestCase(TestCase):
    def setUp(self):
        self.follower = User.objects.create(username="mike6")
        self.following = User.objects.create(username="grace")
        self.following = Following.objects.create(follower=self.follower, following=self.following)

    def test_follow(self):
        self.assertEqual(self.following.follower, self.follower)
        self.assertEqual(self.following.following, self.following)

class ImageTestCase(TestCase):
    def setUp(self):
        self.image = Image(name="sunset")

    def test_likes(self):
        self.assertEqual(self.image.get_likes(), 0)

    def test_update_caption(self):
        self.image.update_caption("nature")
        self.assertEqual(self.shortDescription, "nature")