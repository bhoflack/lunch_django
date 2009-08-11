"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from usecase01 import AdminDepositsToUserAccountTestCase
from BeautifulSoup import BeautifulSoup

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

class AdminDepositsMoneyInUserAccount(TestCase):

    fixtures = ['base.json']

    def setUp(self):
      self.c = Client()

    def test_basic_scenario(self):
      self.c.login(username='admin', password='admin')
      
      response = self.c.get('/products/', {'user' : 'user'})
      doc = BeautifulSoup(response.content)
      print doc.findAll("form")



__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

