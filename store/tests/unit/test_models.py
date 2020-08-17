"""
    To test file images upload I manually pass an image file object
    as in Django Documentation to test the image name, path and url instead of
    testing for 'POST' files requests.
    Django doc about imageFile:
    https://docs.djangoproject.com/en/3.0/topics/files/#the-file-object
"""

from django.test import TestCase
from store.models import Category, Product, new_image_path
from django.core.exceptions import ValidationError
from datetime import date
from django.conf import settings
from django.core.files.images import ImageFile
import shutil


class TestCategory(TestCase):
    """Testing the category model"""

    def test_category_name__str__(self):
        """
        Override '__str__' should return the category's name for
        admin panel
        """

        Category.objects.create(
            name='category test name',
            description='category test description'
        )
        category = Category.objects.first()
        self.assertEqual(str(category), category.name)

    def test_raises_validationError_without_name(self):
        """Should not create category without a name or with empty string"""

        with self.assertRaises(ValidationError):
            Category.objects.create(description='category description')

        with self.assertRaises(ValidationError):
            Category.objects.create(
                name='',
                description='category description')

        with self.assertRaises(ValidationError):
            Category.objects.create(
                name='   ',
                description='category description')

    def test_category_description_is_not_required(self):
        """Can create category without description"""

        Category.objects.create(
            name='category test name')
        category = Category.objects.first()
        self.assertEqual(category.name, 'category test name')


class TestProduct(TestCase):
    """Testing the product model"""

    def setUp(self):

        # Create a dummy product to speed up tests writing
        self.product_data = {
            'name': 'test name',
            'description': 'test description',
            'base_price': 49.99,
        }

    def test_product_name__str__(self):
        """
        Override '__str__' should return the product's name for
        admin panel
        """

        Product.objects.create(**self.product_data)
        product = Product.objects.first()
        self.assertEqual(str(product), product.name)

    def test_product_name_is_required(self):
        """Should not create product without a name or with an empty string"""

        self.product_data['name'] = ''
        with self.assertRaisesMessage(ValidationError, 'Missing name'):
            Product.objects.create(**self.product_data)

        self.product_data['name'] = '    '
        with self.assertRaisesMessage(ValidationError, 'Missing name'):
            Product.objects.create(**self.product_data)

        del self.product_data['name']
        with self.assertRaisesMessage(ValidationError, 'Missing name'):
            Product.objects.create(**self.product_data)

    def test_product_description_is_required(self):
        """Should not create product without a description"""

        self.product_data['description'] = ''
        with self.assertRaisesMessage(ValidationError, 'Missing description'):
            Product.objects.create(**self.product_data)

        self.product_data['description'] = '   '
        with self.assertRaisesMessage(ValidationError, 'Missing description'):
            Product.objects.create(**self.product_data)

        del self.product_data['description']
        with self.assertRaisesMessage(ValidationError, 'Missing description'):
            Product.objects.create(**self.product_data)

    def test_product_base_price_is_required(self):
        """Should not create product without a base_price"""

        del self.product_data['base_price']
        with self.assertRaisesMessage(ValidationError,
                                      'Please set a minimum price of 0.1'):
            Product.objects.create(**self.product_data)

        self.product_data['base_price'] = 0.05
        with self.assertRaisesMessage(ValidationError,
                                      'Please set a minimum price of 0.1'):
            Product.objects.create(**self.product_data)

    def test_product_date_version_auto_now_on_creation(self):
        """
        Product should be automatically created with date_version
        product creation date
        """

        today = date.today()
        product = Product.objects.create(**self.product_data)
        self.assertEqual(product.date_version, today)

    def test_product_image_uploaded_is_renamed(self):
        """
        Product images should be renamed and uploaded to specific path using
        the product.sku UUID field:
        '/media/products/<product_sku>/<new_file_name>.<file_extension>'
        """

        with open(f'{settings.BASE_DIR}/store/tests/_test_file_1.png',
                  'rb') as image_file:
            image = ImageFile(image_file)

            product = Product.objects.create(**self.product_data)
            # 'upload_to' function requires Product instance and image filename
            product.image.save(new_image_path(product, image.name), image)

            # Assert file was renamed
            self.assertNotEqual(str(product.image).rsplit('/')[-1:][0],
                                str(image.name).rsplit('/')[-1:][0])

            # Assert renamed with same extension
            extension_before = str(image.name).rsplit('.')[-1:]
            extension_after = str(product.image.name).rsplit('.')[-1:]
            self.assertEqual(extension_before, extension_after)

            # Assert uploaded to correct path using product's sku
            self.assertEqual('/'.join(str(product.image.url)
                                      .rsplit('/')[:-1]),
                             f'/media/products/{product.sku}')

            # Remove file in directory
            # Comment out to check path & file creation
            product_path = f'media/products/{product.sku}'
            shutil.rmtree(product_path)
