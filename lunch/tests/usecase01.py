import unittest
from django.test import TestCase
from django.test.client import Client


class AdminDepositsToUserAccountTestCase(TestCase):
  fixtures = ['testdata.json']
	
  def setUp(self):
    self.c = Client()
		
  def testMainScenario(self):
    user = 'user'

    # authenticate as admin
    self.c.login(username='admin', password='admin')
    # Admin goes to User's Account page and verifies the current balance
    response = self.c.get("/user/%s" % user, follow=True)
    # Admin adds the amount to the balance
    self.c.post("/user/%s/deposit" % user, {'amount': 5})
    

    
		
