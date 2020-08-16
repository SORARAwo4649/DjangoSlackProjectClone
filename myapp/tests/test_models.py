from django.contrib.auth import get_user_model
from django.test import TestCase

"""
class TestCustomUser(TestCase):
    def test_post_login(self):
        user = get_user_model().objects.create_user('user', password='pass')
        a = user.login_count
        self.assertEqual(user.login_count, a)
        user.post_login()
        self.assertEqual(user.login_count, a+1)
        self.assertEqual(get_user_model().object.get(pk=user.id).login_count, 1)
"""
