from django.test import TestCase
from profile.apps import ProfileConfig
from django.apps import apps


class TestProfileConfig(TestCase):
    """Testing the Profile's app config"""

    def test_app(self):
        """Profile app should be installed as 'profile'"""

        self.assertEqual(ProfileConfig.name, "profile")
        self.assertEqual(apps.get_app_config("profile").name,
                         ProfileConfig.name)
