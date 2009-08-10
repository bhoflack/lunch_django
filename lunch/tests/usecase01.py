import unittest
from django.test import TestCase
from django.test.client import Client


class AdminDepositsToUserAccountTestCase(TestCase):
	fixtures = ['testdata.json']
	
	def setUp(self):
		# prep
		
	def testMainScenario(self):
		