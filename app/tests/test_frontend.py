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
        
    def tearDown(self):
        """Run post each test."""
        pass
        
    def test_input_calc_form_valid(self):
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
        driver.find_element_by_id("patients-weight").send_keys(50)
        driver.find_element_by_id("patients-height").send_keys(150)
        driver.find_element_by_id("patients-serum").send_keys(50)
        driver.find_element_by_id("ctc-button").click()
        self.assertEquals(driver.find_element_by_id("ctc").get_attribute('innerHTML'), 'Creatinine Clearance (Cockcroft-Gault Equation): 104.04 mL/min.', 'Test creatinine calculator function')
        driver.close()
        
    def test_input_calc_form_outlier_young(self):
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
        driver.find_element_by_id("patients-age").send_keys(10)
        driver.find_element_by_id("patients-weight").send_keys(50)
        driver.find_element_by_id("patients-height").send_keys(150)
        driver.find_element_by_id("patients-serum").send_keys(50)
        driver.find_element_by_id("ctc-button").click()
        self.assertEquals(driver.find_element_by_id("warning").get_attribute('innerHTML'), 'This equation should not be used to calculate renal function of children under 12. <br>', 'Test creatinine calculator function')
        driver.close()
        
    def test_input_calc_form_outlier_old(self):
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
        driver.find_element_by_id("patients-age").send_keys(78)
        driver.find_element_by_id("patients-weight").send_keys(50)
        driver.find_element_by_id("patients-height").send_keys(150)
        driver.find_element_by_id("patients-serum").send_keys(50)
        driver.find_element_by_id("ctc-button").click()
        self.assertEquals(driver.find_element_by_id("warning").get_attribute('innerHTML'), 'This equation should not be used to calculate renal function of people over 70. <br>', 'Test creatinine calculator function')
        driver.close()
        
    def test_input_calc_form_invalid_no_sex(self):
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
        driver.find_element_by_id("patients-age").send_keys(27)
        driver.find_element_by_id("patients-weight").send_keys(50)
        driver.find_element_by_id("patients-height").send_keys(150)
        driver.find_element_by_id("patients-serum").send_keys(50)
        driver.find_element_by_id("ctc-button").click()
        self.assertEquals(driver.find_element_by_id("warning").get_attribute('innerHTML'), 'Sex is not selected. <br>', 'Test creatinine calculator function')
        driver.close()
        
    def test_input_search_BNF_table_name(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/dashboard/home/')
        delay = 10 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "calculator-opener")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        
        #Send some text to the input boxes and click on the calculate button
        driver.find_element_by_id("myInput").send_keys('Alum')
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "BNFbody")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        self.assertEquals(len(driver.find_element_by_id("BNFbody").find_elements_by_css_selector("*")), 15, 'Test BNF table searchbox function')
        driver.close()
    
    def test_input_search_BNF_table_code(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/dashboard/home/')
        delay = 10 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "calculator-opener")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        
        #Send some text to the input boxes and click on the calculate button
        driver.find_element_by_id("myInput").send_keys('050104')
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "BNFbody")))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        self.assertEquals(len(driver.find_element_by_id("BNFbody").find_elements_by_css_selector("*")), 30, 'Test BNF table searchbox function')
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