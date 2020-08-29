"""
    An existing product is required to test products related views and urls.
    The image field is required in Product and images are saved in
    '/media/<product_sku>/'.
    Use setUp and tearDown to clean files each time the test is run, especially
    in case of failures.
    Details of image file testing in 'test_models.py'
"""
from django.test import TestCase
from store.models import Product, new_image_path, Category
from django.conf import settings
from django.core.files.images import ImageFile
import shutil


class TestStoreUrls(TestCase):
    """Test Store app urls"""

    def setUp(self):
        # Create a product with its image file
        self.product_data = {
            'name': 'test product name',
            'description': 'test product description',
            'base_price': 49.99,
        }
        with open(f'{settings.BASE_DIR}/store/tests/_test_file_1.png',
                  'rb') as image_file:
            image = ImageFile(image_file)

            self.product = Product(**self.product_data)
            self.product.image.save(
                new_image_path(self.product, image.name), image)
            self.product.save()

    def tearDown(self):
        # Remove file in directory after tests
        # Comment out to check path & file creation
        product_path = f'media/products/{self.product.sku}'
        shutil.rmtree(product_path)

    def test_store_landing_url(self):
        """Test Store landing page url and used template"""

        store_page = self.client.get("/store/")
        self.assertEqual(store_page.status_code, 200)
        self.assertTemplateUsed(store_page, 'store/store.html')

    def test_product_details_url(self):
        """Test Store's product details url and used template"""

        product_page = self.client.get(f'/store/{self.product.id}/')
        self.assertEqual(product_page.status_code, 200)
        self.assertTemplateUsed(product_page, 'store/product_details.html')

    def test_store_search_toolbar(self):
        """Test Store's search toolbar returns results to store template"""

        product_page = self.client.get('/store/', {'q': self.product.name})
        self.assertEqual(product_page.status_code, 200)
        self.assertTemplateUsed(product_page, 'store/store.html')

    def test_store_browse_category(self):
        """Test Store's category browsing returns results to store templates"""

        category = Category.objects.create(name='category test name')

        category_page = self.client.get('/store/', {'category': category.name})
        self.assertEqual(category_page.status_code, 200)
        self.assertTemplateUsed(category_page, 'store/store.html')
