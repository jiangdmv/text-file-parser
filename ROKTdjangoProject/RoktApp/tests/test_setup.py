from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    # the following 2 functions will be run when run the test.
    def setUp(self):
        self.upload_url = reverse('upload-list')
        self.app_url = reverse('app')

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


