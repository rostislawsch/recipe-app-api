from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
# reverse() allows us to generate URLs for our Django Admin page


class AdminSiteTests(TestCase):
    # setup function. sometime there is stuff to do before the test runs
    # this will be done by our setup function
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@testsite.com', password='test1234')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='admin@testsite.com',
            password='test1234',
            name='test user full name')

    # we test that the users are listed in our django admin
    # the reason we test this is, because we are slightly custimizin
    # our user model
    # default user model expects a usermane, we chahge it to email

    def test_users_listed(self):
        """ test that users are listed on the page """
        # these URLs are defined in the django admin documentation
        # the function below will generate the list url for out user page
        # if we wanna change the url in the future the test will still run
        url = reverse('admin:core_user_changelist')
        # this will use our test client to perform an
        # HTTP GET request on the URL that we found above
        res = self.client.get(url)
        # the assertContains is a django custom assertion that will check
        # that our response contains a certain item
        # also checks if response code is 200 and more stuff
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        # test that the user edit page works
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/:id, so anything we pass in args will be assigned
        # to the arguments of the URL
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        # test that the create user page works
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
