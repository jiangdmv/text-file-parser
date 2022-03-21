from .test_setup import TestSetUp


class TestCase(TestSetUp):

    def test_upload(self):
        res = self.client.post(self.upload_url)
        self.assertEqual(res.status_code, 400)

    def test_app(self):
        data = {"filename":"sample1.txt", "from":"2021-07-06T23:00:00Z", "to": "2020-07-06T23:00:00Z"}
        res = self.client.post(self.app_url, data, format='json')
        self.assertEqual(res.status_code, 404)

    def test_app1(self):
        data = {"filename":"sample.txt", "from":"2001-01-06T23:00:00Z", "to": "2001-07-06T23:00:00Z"}
        res = self.client.post(self.app_url, data, format='json')
        self.assertEqual(res.status_code, 200)