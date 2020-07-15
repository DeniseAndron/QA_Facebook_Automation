from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
import unittest
#import the file with the password and username
from selenium.webdriver.common.action_chains import ActionChains


class Sign_Up(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Denisa/Desktop/selenium/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://www.facebook.com/")

    def test_sign(self):
        driver = self.driver

        first_name = driver.find_element_by_xpath('//input[@name="firstname"]').send_keys("rifinder")
        surname = driver.find_element_by_xpath('//input[@name="lastname"]').send_keys("testing")
        email = driver.find_element_by_xpath('//input[@name="reg_email__"]').send_keys("testing@gmail.com")
        sleep(1)
        c_email = driver.find_element_by_xpath('//input[@name="reg_email_confirmation__"]').send_keys(
            "testing@gmail.com")
        password = driver.find_element_by_xpath('//input[@name="reg_passwd__"]').send_keys("testing")

        day = Select(driver.find_element_by_xpath('//select[@id="day"]'))
        # select by visible text
        day.select_by_visible_text("4")

        month = Select(driver.find_element_by_xpath('//select[@id="month"]'))
        # select by index
        month.select_by_index(4)

        year = Select(driver.find_element_by_xpath('//select[@id="year"]'))
        # select by value
        year.select_by_value("1996")

        sleep(2)

        gender = driver.find_element_by_xpath('//input[@id="u_0_6"]')
        # check if the gender is selected
        verify_gender = gender.is_selected()
        print(verify_gender)
        if verify_gender != True:
            gender = driver.find_element_by_xpath('//input[@id="u_0_6"]')
            gender.click()
        verify_gender = gender.is_selected()
        print(verify_gender)

        sleep(5)
        submit = driver.find_element_by_link_text("Sign Up")
        submit.click()

        sleep(5)

    #wrong password
    def test_login_wrong(self):
        driver = self.driver

        #Login

        login = driver.find_element_by_xpath('//input[@id="email"]').send_keys("testing@gmail.com")
        pw = driver.find_element_by_xpath('//input[@id="pass"]').send_keys("testing")
        sleep(3)
        login_button = driver.find_element_by_xpath('//input[@id="u_0_b"]').click()
        sleep(5)




if __name__ == "__main__":
    unittest.main()  #it will run everytest case



