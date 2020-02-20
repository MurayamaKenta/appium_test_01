# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["automationName"] = "Appium"
caps["platformVersion"] = "8.0"
caps["deviceName"] = "Android Emulator"
caps["app"] = "/Users/murayamakenta/Downloads/test/app-rc.apk"
caps["appWaitDuration"] = 10000
caps["appWaitActivity"] = "com.quipper.school.assignment.ui.start.login.LoginActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el3 = driver.find_element_by_id("jp.studysapuri.android.rc:id/username_V")
el3.send_keys("6901")
el4 = driver.find_element_by_id("jp.studysapuri.android.rc:id/password_V")
el4.send_keys("quipper123")
el5 = driver.find_element_by_id("jp.studysapuri.android.rc:id/login_B")
el5.click()


driver.quit()