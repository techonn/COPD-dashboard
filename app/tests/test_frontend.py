import unittest
from os import getcwd
from selenium import webdriver

class TestWebForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        
    def test_input_form(self):
        path= getcwd()
        driver = self.driver
        driver.get('file:///'+ path +'app/templates/index.html')
        
        #Send some text to the input boxes and click on the calculate button
        driver.find_element_by_id("sex").send_keys('f')
        driver.find_element_by_id("patients-age").send_keys(27)
        driver.find_element_by_id("patients-weight").send_keys(51)
        driver.find_element_by_id("patients-serum").send_keys(1)
        driver.find_element_by_id("Submit").click()
        
        self.assertEquals(driver.find_element_by_id("ctc-results"), 68.04, 'Test creatinine calculator function')
        
        
if __name__=="__main__":
    unittest.main()