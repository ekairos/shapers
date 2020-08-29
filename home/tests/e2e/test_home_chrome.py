from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestChromeHome(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_terms_use(self):
        self.selenium.get(f'{self.live_server_url}/')
        WebDriverWait(self.selenium, 10).until(EC.url_changes)
        self.selenium.find_element_by_xpath("//a[@href='/terms-use/']")\
            .click()
        self.assertRegex(self.selenium.current_url, "/terms-use/$")

    def test_privacy_policy(self):
        self.selenium.get(f'{self.live_server_url}/')
        WebDriverWait(self.selenium, 10).until(EC.url_changes)
        self.selenium.find_element_by_xpath("//a[@href='/privacy-policy/']")\
            .click()
        self.assertRegex(self.selenium.current_url, "/privacy-policy/$")

    def test_about_us(self):
        self.selenium.get(f'{self.live_server_url}/')
        WebDriverWait(self.selenium, 10).until(EC.url_changes)
        self.selenium.find_element_by_xpath("//a[@href='/about-us/']")\
            .click()
        self.assertRegex(self.selenium.current_url, "/about-us/$")

    def test_home_page(self):
        self.selenium.get(f'{self.live_server_url}/about-us/')
        WebDriverWait(self.selenium, 10).until(EC.url_changes)
        self.selenium.find_element_by_class_name("navbar-brand")\
            .click()
        self.assertEqual(self.selenium.current_url, f'{self.live_server_url}/')
