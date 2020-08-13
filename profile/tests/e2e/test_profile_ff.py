from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProfileFirefox(StaticLiveServerTestCase):
    """Testing Profile app interaction with Firefox"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = Firefox()
        cls.selenium.implicitly_wait(5)

        cls.new_user = {
            'email': 'whatever@gmail.net',
            'password': 'Aaaa2468',
            'username': 'johnny',
            'first_name': 'john',
            'last_name': 'Doe',
        }

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def _to_signin(self):
        """Navbar dropdown signin should redirect to sign in page"""

        self.selenium.find_element_by_link_text('Account').click()
        self.selenium.find_element_by_link_text('Sign In').click()
        self.assertEqual(self.selenium.current_url,
                         f'{self.live_server_url}/accounts/login/')

        self.selenium.find_element_by_id('id_login').send_keys(
            self.new_user['email'])
        self.selenium.find_element_by_id('id_password').send_keys(
            self.new_user['password'])
        self.selenium.find_element_by_xpath(
            "//form[@action='/accounts/login/']//button[@type='submit']"
        ).click()

    def _to_signup(self):
        """
        Navbar dropdown signup should redirect to sign up page.
        Successful registration should redirect to home page
        """

        self.selenium.find_element_by_link_text('Account').click()
        self.selenium.find_element_by_link_text('Sign Up').click()
        self.assertEqual(self.selenium.current_url,
                         f'{self.live_server_url}/accounts/signup/')

        self.selenium.find_element_by_id('id_email').send_keys(
            self.new_user['email'])
        self.selenium.find_element_by_id('id_email2').send_keys(
            self.new_user['email'])
        self.selenium.find_element_by_id('id_username').send_keys(
            self.new_user['username'])
        self.selenium.find_element_by_id('id_first_name').send_keys(
            self.new_user['first_name'])
        self.selenium.find_element_by_id('id_last_name').send_keys(
            self.new_user['last_name'])
        self.selenium.find_element_by_id('id_password1').send_keys(
            self.new_user['password'])
        self.selenium.find_element_by_id('id_password2').send_keys(
            self.new_user['password'])
        self.selenium.find_element_by_xpath(
            "//form[@id='signup_form']//button[@type='submit']").click()
        WebDriverWait(self.selenium, 10).until(EC.url_changes)
        self.assertEqual(self.selenium.current_url,
                         f'{self.live_server_url}/')

    def _to_profile(self):
        """
        Authenticated users should access My Profile page from navbar dropdown
        """

        self.selenium.find_element_by_link_text('My Account').click()
        self.selenium.find_element_by_link_text('My Profile').click()
        self.assertEqual(self.selenium.current_url,
                         f'{self.live_server_url}/profile/')

    def _logout(self):
        """
        Autheticated users can logout from the MyAccount navbar dropdown
        """

        self.selenium.find_element_by_link_text('My Account').click()
        self.selenium.find_element_by_link_text('Logout').click()
        WebDriverWait(self.selenium, 10).until(EC.url_changes)
        self.assertEqual(self.selenium.current_url,
                         f'{self.live_server_url}/accounts/logout/')
        self.selenium.find_element_by_xpath(
            "//form[@action='/accounts/logout/']//button[@type='submit']"
        ).click()
        WebDriverWait(self.selenium, 10).until(EC.url_changes)
        self.assertEqual(self.selenium.current_url,
                         f'{self.live_server_url}/')

    def test_authentication(self):
        """
        Test grouping registration, My Profile access, logout and
        login process.
        """

        self.selenium.get(f'{self.live_server_url}/')

        self._to_signup()

        self._to_profile()

        self._logout()

        self._to_signin()
