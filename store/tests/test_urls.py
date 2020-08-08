from django.test import TestCase


class TestStoreUrls(TestCase):
    """Test Store app urls"""

    def test_store_landing_url(self):
        """Test Store landing page url and used template"""

        store_page = self.client.get("/store/")
        self.assertEqual(store_page.status_code, 200)
        self.assertTemplateUsed(store_page, 'store/store.html')
