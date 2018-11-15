import unittest
import time
from selenium import webdriver


class addServiceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_service(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://foodserviceapp.herokuapp.com/accounts/login/")
        time.sleep(2)
        # elem = driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/p[2]/a[1]").click()
        # time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        print("Logged in")
        time.sleep(1)
        # Click View details under Service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(1)
        # Click Add Service button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Barbara York")
        time.sleep(1)
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Food Prep/Delivery")
        time.sleep(1)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Sandwich Lunch and Beverages - 30")
        time.sleep(1)
        elem = driver.find_element_by_id("id_location")
        elem.send_keys("PKI Room 270")
        time.sleep(1)
        # elem = driver.find_element_by_id("id_setup_time")
        # elem.send_keys("2018-11-09 17:31:26")
        # time.sleep(1)
        # elem = driver.find_element_by_id("initial-id_cleanup_time")
        # elem.send_keys("2018-11-09 17:31:26")
        # time.sleep(1)
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("260")
        time.sleep(1)
        # Click Save
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        print("Added Service successfully")
        # driver.get("http://127.0.0.1:8000")
        # time.sleep(1)
        # driver.get("http://127.0.0.1:8000")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
