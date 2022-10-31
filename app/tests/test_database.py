"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
#from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.db_mod = Database()

    def tearDown(self):
        """Run post each test."""
        pass

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
        self.assertEquals(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')
    
    def test_get_average_ACT(self):
        """Test that the average of actual cost returns the correct value."""
        self.assertEquals(self.db_mod.get_average_ACT(), 76.221, 'Test average act cost returns correct value')

    def test_get_percentage_of_top_item(self):
        """Test that the percentage of top item returns the correct value."""
        self.assertEquals(self.db_mod.get_percentage_of_top_item(), 2.75, 'Test top item returns correct value')

    def test_get_unique_number_of_items(self):
        """Test that the unique number of items returns the expected value."""
        self.assertEquals(self.db_mod.get_unique_number_of_items(), 13935, 'Test_for_expected value')

if __name__ == "__main__":
    unittest.main()