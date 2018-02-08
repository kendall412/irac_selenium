import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

site = "http://10.132.6.183"

username = "root"
password = "calvin"
server = "R940"

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get(site)

# LOGIN -------------------------------------------------------------------
xpath_server_name = "PowerEdge R940"
xpath_username = "//input[starts-with(@class,'cui-start-screen-username')]"
xpath_password = "//input[starts-with(@class,'cui-start-screen-password')]"
xpath_button = "//button[starts-with(@class,'cux-button')]"

# CONFIGURATION -----------------------------------------------------------
xpath_configuration = "//strong[starts-with(@class,'ng-scope')]"
configuration_link_text = "Configuration"

# server_name = driver.find_element(By.PARTIAL_LINK_TEXT,xpath_server_name)

time.sleep(1)
username_text_field = driver.find_element(By.XPATH,xpath_username)
password_text_field = driver.find_element(By.XPATH,xpath_password)
login_button = driver.find_element(By.XPATH,xpath_button)


print "driver.title is " + driver.title
if server.lower() in driver.title:
	print "this is the correct server"
elif server.lower() not in driver.title:
	print "this is not the correct server"

time.sleep(1)
username_text_field.clear()
username_text_field.send_keys(username)

time.sleep(1)
password_text_field.clear()
password_text_field.send_keys(password)
login_button.click()

# configuration_tab = driver.find_element(By.LINK_TEXT, configuration_link_text)
# configuration_tab = driver.find_element(By.LINK_TEXT, xpath_configuration)
# configuration_tab.click()

# time.sleep(5)
# driver.close()