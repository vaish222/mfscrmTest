#Vaishali Goel
import unittest
import time
from selenium import webdriver


class deleteServiceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_delete_service(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://foodserviceapp.herokuapp.com/accounts/login/")
        time.sleep(1)
        # elem = driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/p[2]/a[1]").click()
        # time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        assert "Logged in"
        time.sleep(1)
        # Click View details under Service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)
        # Click Delete Service button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[5]/td[9]/a").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)
        assert "Deleted Service successfully"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
