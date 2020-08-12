from django.test import TestCase


class TestProfileUrls(TestCase):
    """Test Profile app urls"""

    def test_profile_page_url(self):
        """
        Unauthenticated users should be redirected from profile to login page
        """

        profile_page = self.client.get("/profile/")
        self.assertEqual(profile_page.status_code, 302)
        self.assertRegex(profile_page.url, "^/accounts/login/")
