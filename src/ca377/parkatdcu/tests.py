from django.test import TestCase
from django.urls import reverse

class SetUpTest(TestCase):

    def test_welcome(self):
      """
      The index page loads and an appropriate welcome message is displayed
      """
      response = self.client.get(reverse('parkatdcu:index'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "Welcome to ParkAtDCU")
