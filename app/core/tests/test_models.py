from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """
        creating new user is successful
        """
        email = 'rashokmpi@gmail.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        # self.assertEqual(user.check_password(password))
    def test_normalize_email(self):
        email ='rashokmpi@gMIAL.COM'
        user = get_user_model().objects.create_user(email, 'fkvk4320')

        self.assertEqual(user.email, email.lower())

    def test_new_email_validation(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'sfvnkj4')

    def create_new_super_user(self):
        """
        Test Create new super user
        """
        user = get_user_model().objects.create_user('rashokmpi@gmail.com', 'fkvk4320')
        self.assertTrue(user.is_super_user)
        self.assertTrue(user.is_staff)
