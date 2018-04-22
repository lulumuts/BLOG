import unittest
from app.models import Posts


class PostsTest(unittest.TestCase):
        '''
        Test Class to test the behaviour of the posts Class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''

            self.new_posts = Posts(1234, 'Python Must Be Crazy','A thrilling new Python Series','whatever',31-09-18,4657)

        def test_instance(self):
            self.assertTrue(isinstance(self.new_posts,Posts))
