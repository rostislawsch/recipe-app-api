from django.test import TestCase
from django.contrib.auth import get_user_model
# wir importieren das, damit wir später das user model ändern können

class ModelTests(TestCase):
    # wir testen, ob unsere create user function einen neuen user kreiert
    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'test@rostislaw.com'
        password = "Testpass1234"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email, email)
        # check_password() is a helper function that comes with the django user model.
        # it returns true, if the passwprd is correct and false if not
        self.assertTrue(user.check_password(password))