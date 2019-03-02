import unittest
from app.models import Comment

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(id =1, usernames = 'nicole',comment= 'I love this post',blog_id=3,user_id= 2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
