import unittest
from app.models import Comments


class CommentsTest(unittest.TestCase):
        '''
        Test Class to test the behaviour of the Comments Class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''

            self.new_posts = Posts(1234, 'Python Must Be Crazy','A thrilling new Pyton Series',3827)

        def test_instance(self):
            self.assertTrue(isinstance(self.new_comment,Comments))
