from django.test import TestCase
from profile.forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def setUp(self):
        self.user_profile = {
            'profile_phone_number': '+123456789',
            'profile_street_address1': 'Street Address 1',
            'profile_street_address2': 'Street Address 2',
            'profile_postcode': 'P123',
            'profile_town_or_city': 'Town or City',
            'profile_country': 'Country',
        }

    def test_street_address1_required(self):

        del self.user_profile['profile_street_address1']
        form = UserProfileForm(data=self.user_profile)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['profile_street_address1'][0],
                         'This field is required.')

    def test_postcode_required(self):

        del self.user_profile['profile_postcode']
        form = UserProfileForm(data=self.user_profile)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['profile_postcode'][0],
                         'This field is required.')

    def test_town_city_required(self):

        del self.user_profile['profile_town_or_city']
        form = UserProfileForm(data=self.user_profile)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['profile_town_or_city'][0],
                         'This field is required.')

    def test_country_required(self):

        del self.user_profile['profile_country']
        form = UserProfileForm(data=self.user_profile)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['profile_country'][0],
                         'This field is required.')

    def test_phone_and_address2_not_required(self):
        del self.user_profile['profile_phone_number']
        del self.user_profile['profile_street_address2']
        form = UserProfileForm(data=self.user_profile)
        self.assertTrue(form.is_valid())
        self.assertNotIn('profile_phone_number', form.errors.keys())
        self.assertNotIn('profile_street_address2', form.errors.keys())
