from django.test import TestCase


class TestProfileUrls(TestCase):
    """Test Profile app urls"""

    def test_home_page_url(self):
        """Test profile page url"""

        profile_page = self.client.get("/profile/")
        self.assertEqual(profile_page.status_code, 200)
        self.assertTemplateUsed(profile_page, 'profile/profile.html')
