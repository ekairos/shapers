from django.test import TestCase
from profile.models import UserProfile, User


class TestUserProfileModel(TestCase):
    """Testing UserProfile model"""

    def setUp(self):
        self.user_data = {
            'username': 'test username',
            'email': 'test@mail.net',
            'first_name': 'John',
            'last_name': 'Doe',
            'password': 'Aaaa2468'
        }

    def test_user_profile__str__(self):
        """
        __str__ method should return username or a string containing firstname,
        lastname and username if all provided
        """

        user = User.objects.create(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password='Aaaa2468')
        user_profile = UserProfile.objects.first()
        self.assertEqual(str(user_profile), self.user_data['username'])
        user.delete()

        user = User.objects.create(**self.user_data)
        user_profile = UserProfile.objects.first()
        self.assertEqual(str(user_profile), f"{self.user_data['first_name']} "
                                            f"{self.user_data['last_name']} "
                                            f"as {self.user_data['username']}")
        user.delete()

    def test_user_profile_created_with_new_user(self):
        """User's profile should be automatically created on signup"""

        user_profile = UserProfile.objects.first()
        self.assertFalse(user_profile)

        user = User.objects.create(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password='Aaaa2468')
        user_profile = UserProfile.objects.first()
        self.assertTrue(user_profile)

        user.delete()

    def test_user_profile_deleted_with_user(self):
        """
        User's profile should be automatically deleted when user delete account
        """

        user = User.objects.create(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password='Aaaa2468')
        user_profile = UserProfile.objects.first()
        self.assertTrue(user_profile)

        user.delete()
        user_profile = UserProfile.objects.first()
        self.assertFalse(user_profile)
