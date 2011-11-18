import unittest
from pyramid.config import Configurator
from pyramid import testing

def _initTestingDB():
    pass
class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        

    def tearDown(self):
        testing.tearDown()

    def test_it(self):
        from contacts.views import home
        request = testing.DummyRequest()
        info = home(request)
        self.assertEqual(info['project'], 'Contacts')
