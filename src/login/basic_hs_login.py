# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# coding: utf-8

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from Connection import app_connection



# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


driver = app_connection.driver()


el4 = driver.find_element_by_id("jp.studysapuri.android.rc:id/username_V")
el4.send_keys("5321")

el5 = driver.find_element_by_id("jp.studysapuri.android.rc:id/password_V")
el5.send_keys("quipper123")

el6 = driver.find_element_by_id("jp.studysapuri.android.rc:id/login_B")
el6.click()


time.sleep(7) 

driver.quit()



