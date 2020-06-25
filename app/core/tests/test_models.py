from django.test import TestCase
from django.contrib.auth import get_user_model
# wir importieren das, damit wir später das user model ändern können


class ModelTests(TestCase):

    # wir testen, ob unsere create user function einen neuen user kreiert
    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'test@testsite3.com'
        password = "Testpass1234"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        # check_password() is a helper function that comes
        # with the django user model.
        # it returns true, if the passwprd is correct and false if not
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for new user is normalized """
        email = "test@testSITE2.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test123@testsite4.com', 'test1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
