import unittest
from app import app
from app.database.controllers import Database
import os

class ViewTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        """Run post each test."""
        pass
    
    def test_home(self):
        result = self.app.get('/dashboard/home/')
        input_file = open(os.getcwd()+"\\app\\tests\\test_html.html", mode="r", encoding="utf-8")
        # Make your assertions
        self.assertEquals(result.data.decode(), input_file.read(),'Test the requested session of dashboard home')

if __name__ == "__main__":
    unittest.main()