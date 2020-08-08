from django.test import TestCase
from store.apps import StoreConfig
from django.apps import apps


class TestStoreConfig(TestCase):
    """Testing Store's app config"""

    def test_app(self):
        """Store app should be installed as 'store'"""

        self.assertEqual(StoreConfig.name, "store")
        self.assertEqual(apps.get_app_config("store").name, StoreConfig.name)
