from django.test import TestCase
from  home.apps import HomeConfig
from django.apps import apps


class TestHomeConfig(TestCase):
    """Testing the Home's app config"""

    def test_app(self):
        """Home app should be installed as 'home'"""

        self.assertEqual(HomeConfig.name, "home")
        self.assertEqual(apps.get_app_config("home").name, HomeConfig.name)
