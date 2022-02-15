import unittest
from models import quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote("Jamie Zawinski",4,"Some people, when confronted with a problem, think \u201cI know, I\u2019ll use regular expressions.\u201d Now they have two problems.","http://quotes.stormconsultancy.co.uk/quotes/4")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()