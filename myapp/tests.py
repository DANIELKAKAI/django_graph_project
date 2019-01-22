from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class AppTest(TestCase):
    def test_view(self):
        url = reverse("graph")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


