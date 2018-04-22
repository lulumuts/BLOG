import unittest
from app.models import Subscription


class SubscriptionTest(unittest.TestCase):
        '''
        Test Class to test the behaviour of the subscription Class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''

            self.new_subscriber = Subscription(1234, 'Python Must Be Crazy','A thrilling new Python Series')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_subscriber,Subscription))
