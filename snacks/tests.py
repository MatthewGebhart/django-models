from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_list_status_code(self):
        url = reverse('snack_list')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_detail_status_code(self):
        url = reverse('snack_detail', args=(1,))
        print(f'the url is: {url}')
        response = self.client.get(url)
        print(f'this is the response{response}')
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_template(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')
