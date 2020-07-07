#open browser with the automatic software selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/Denisa/Desktop/selenium/chromedriver_win32/chromedriver.exe"


#Filling up the sign up form


driver = webdriver.Chrome(path)

driver.get("https://www.facebook.com/")
time.sleep(3)
first_name = driver.find_element_by_xpath('//input[@name="firstname"]').send_keys("rifinder")
surname = driver.find_element_by_xpath('//input[@name="lastname"]').send_keys("testing")
email = driver.find_element_by_xpath('//input[@name="reg_email__"]').send_keys("testing@gmail.com")
time.sleep(1)
c_email = driver.find_element_by_xpath('//input[@name="reg_email_confirmation__"]').send_keys("testing@gmail.com")
password = driver.find_element_by_xpath('//input[@name="reg_passwd__"]').send_keys("testing")


day = Select(driver.find_element_by_xpath('//select[@id="day"]'))
#select by visible text
day.select_by_visible_text("4")

month = Select(driver.find_element_by_xpath('//select[@id="month"]'))
#select by index
month.select_by_index(4)

year = Select(driver.find_element_by_xpath('//select[@id="year"]'))
#select by value
year.select_by_value("1996")

time.sleep(2)

gender = driver.find_element_by_xpath('//input[@id="u_0_6"]')
#check if the gender is selected
verify_gender = gender.is_selected()
if verify_gender != True:
    gender = driver.find_element_by_xpath('//input[@id="u_0_6"]')
    gender.click()
verify_gender = gender.is_selected()
print(verify_gender)

time.sleep(2)


