import unittest
from markdown import markdown
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class TestWebForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        
    def test_input_calc_form(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/dashboard/home/')
        delay = 10 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "calculator-opener")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        
        #Send some text to the input boxes and click on the calculate button
        driver.find_element_by_id("calculator-opener").click()
        driver.find_element_by_id("sexf").click()
        driver.find_element_by_id("patients-age").send_keys(27)
        driver.find_element_by_id("patients-weight").send_keys(51)
        driver.find_element_by_id("patients-serum").send_keys(1)
        driver.find_element_by_id("ctc-button").click()
        self.assertEquals(float(driver.find_element_by_id("ctc").get_attribute('innerHTML')), 68.04, 'Test creatinine calculator function')
        driver.close()
    
    def test_about_popup(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/dashboard/home/')
        delay = 10 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "about-text")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        driver.find_element_by_id("about-text").click()
        driver.close()

    def test_print_pdf(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/dashboard/home/')
        delay = 10 #seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,"about-text1")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        driver.find_element_by_id("pdfconvert").click()
        driver.close()
if __name__=="__main__":
    unittest.main()