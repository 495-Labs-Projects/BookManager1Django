from selenium import webdriver

from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from books.tests.utilities import *


class FactoryFunctionalTestCase(StaticLiveServerTestCase):
    factories = Populate()    

class FunctionalTest(FactoryFunctionalTestCase):

    def setUp(self):
        # Download chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
        # place it in the drivers folder and change the following path
        # You can also use Firefox's greckodriver https://github.com/mozilla/geckodriver/releases
        self.selenium = webdriver.Chrome(executable_path="books/tests/drivers/chromedriver.exe")
        self.selenium.implicitly_wait(3)
        self.factories.populate_books()

    def tearDown(self):
        # May need close for Mac/Linux
        # Needs close for Firefox
        # self.selenium.close()
        pass

    # Auxiliary function to add view subdir to URL
    def _get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_books_list(self):
        self.selenium.get(self._get_full_url("books:book_list"))
        self.assertIn('Book Manager', self.selenium.title)
