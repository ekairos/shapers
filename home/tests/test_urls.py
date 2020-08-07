from django.test import TestCase


class TestHomeUrls(TestCase):
    """Test Home app urls"""

    def test_home_page_url(self):
        """Test home page url"""

        home_page = self.client.get("/")
        self.assertEqual(home_page.status_code, 200)
        self.assertTemplateUsed(home_page, 'home/index.html')

    def test_about_us_url(self):
        """Test about us url"""

        about_page = self.client.get("/about-us/")
        self.assertEqual(about_page.status_code, 200)
        self.assertTemplateUsed(about_page, 'home/about_us.html')

    def test_privacy_policy_url(self):
        """Test privacy policy url"""

        privacy_page = self.client.get("/privacy-policy/")
        self.assertEqual(privacy_page.status_code, 200)
        self.assertTemplateUsed(privacy_page, 'home/privacy_policy.html')
