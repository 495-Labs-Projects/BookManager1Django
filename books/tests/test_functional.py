from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from books.tests.utilities import *


class FactoryFunctionalTestCase(StaticLiveServerTestCase):
    factories = Populate()

    # Auxiliary function to add view subdir to URL
    def get_full_url(self, url):
        return self.live_server_url + url

    # Wait page load by element id presence
    def wait_page_load(self, id):
        wait = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )


class BookFunctionalTest(FactoryFunctionalTestCase):

    def setUp(self):
        # Download Firefox's greckodriver https://github.com/mozilla/geckodriver/releases
        # place it in the drivers folder and change the following path
        # You can also use chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
        # Make sure to use webdriver.Chrome instead if you are using Chrome
        self.driver = webdriver.Firefox(executable_path="books/tests/drivers/geckodriver.exe")
        self.driver.implicitly_wait(3)
        self.factories.populate_books()

    def tearDown(self):
        self.driver.quit()

    def test_book_list(self):
        driver = self.driver
        self.driver.get(self.get_full_url(reverse("books:book_list")))

        self.assertIn('Book Manager', driver.title)
        heading = driver.find_element_by_css_selector("h1")
        self.assertIn('Books', heading.text)

        books = driver.find_elements_by_css_selector("#book-list li")
        self.assertEqual(len(books), Book.objects.count())

    def test_book_detail(self):
        driver = self.driver
        self.driver.get(self.get_full_url(reverse("books:book_detail", args=(self.factories.b1.id,))))

        title = driver.find_element_by_id("book-title")
        self.assertEqual(self.factories.b1.title, title.text)

        authors = driver.find_elements_by_css_selector("#book-authors li")
        self.assertEqual(len(authors), self.factories.b1.authors.count())

    def test_create_new_book(self):
        driver = self.driver
        self.driver.get(self.get_full_url(reverse("books:book_new")))

        title_input = driver.find_element_by_id("id_title")
        title_input.send_keys('Test Title')

        year_published_input = driver.find_element_by_id("id_year_published")
        year_published_input.clear()
        year_published_input.send_keys('1990')

        publisher_input = driver.find_element_by_id("id_publisher")
        publisher_input.find_element_by_css_selector("option[value='%s']" % self.factories.p1.id).click()

        authors_input = driver.find_element_by_id("id_authors")
        authors_input.find_element_by_css_selector("input[value='%s']" % self.factories.a1.id).click()

        authors_input.submit()

        self.wait_page_load("book-title")

        title = driver.find_element_by_id("book-title")
        self.assertEqual('Test Title', title.text)

