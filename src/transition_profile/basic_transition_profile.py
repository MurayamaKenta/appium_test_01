# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# from appium import webdriver

# caps = {}
# caps["platformName"] = "Android"
# caps["automationName"] = "Appium"
# caps["platformVersion"] = "8.0"
# caps["deviceName"] = "Android Emulator"
# caps["app"] = "/Users/murayamakenta/Downloads/test/app-rc.apk"
# caps["appWaitDuration"] = 10000
# caps["appWaitActivity"] = "com.quipper.school.assignment.ui.start.login.LoginActivity"

# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from Connection import app_connection


driver = app_connection.driver()

el1 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"icon\"])[3]")
el1.click()
el2 = driver.find_element_by_accessibility_id("プロフィール")
el2.click()

time.sleep(5)

driver.quit()