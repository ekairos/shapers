from django.test import TestCase


class TestHomeUrls(TestCase):
    """Test Home app urls"""

    def test_home_page_url(self):
        """Test home page url"""

        home_page = self.client.get("/")
        self.assertEqual(home_page.status_code, 200)
        self.assertTemplateUsed(home_page, 'home/index.html')
