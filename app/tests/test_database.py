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
        self.assertEquals(self.db_mod.get_average_ACT(), 76.22065025148007, 'Test average act cost returns correct value')

    def test_get_top_prescribed_item(self):
        """Test that the top prescribed item returns the correct value."""
        self.assertEquals(self.db_mod.get_top_prescribed_item(), 'Omeprazole_Cap E/C 20mg', 'Test top prescribed item returns correct value')

    def test_get_percentage_of_top_item(self):
        """Test that the percentage of top item returns the correct value."""
        self.assertEquals(self.db_mod.get_percentage_of_top_item(), 2.75, 'Test top item returns correct value')

    def test_get_unique_number_of_items(self):
        """Test that the unique number of items returns the expected value."""
        self.assertEquals(self.db_mod.get_unique_number_of_items(), 13935, 'Test_for_expected value')

    def test_get_percentage_of_inf_drug_gr(self):
        """Test that the unique number of items returns the expected value."""
        self.assertEquals(self.db_mod.get_percentage_of_inf_drug_gr(), [('Antibacterial', 0.7971759046162527), ('Antifungal', 0.08877637381401357), ('Antiviral', 0.02680069488782313), ('Antiprotozoal', 0.08520171049310309), ('Anthelmintics', 0.002045316188807555)], 'Test_for_expected list of percentages')

if __name__ == "__main__":
    unittest.main()