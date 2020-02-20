# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction




caps = {}
caps["platformName"] = "Android"
caps["automationName"] = "Appium"
caps["platformVersion"] = "8.0"
caps["deviceName"] = "Android Emulator"
caps["app"] = "/Users/murayamakenta/Downloads/test/app-rc.apk"
caps["appWaitDuration"] = 10000
caps["appWaitActivity"] = "com.quipper.school.assignment.ui.start.login.LoginActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


# -----transition profile-----
# el5 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"icon\"])[4]")
# el5.click()
# el6 = driver.find_element_by_accessibility_id("プロフィール")
# el6.click()
# -----transition profile-----

TouchAction(driver)   .press(x=531, y=2035)   .move_to(x=544, y=254)   .release()   .perform()

 
    
el7 = driver.find_element_by_id("jp.studysapuri.android.rc:id/logout_TV")
el7.click()
el8 = driver.find_element_by_id("jp.studysapuri.android.rc:id/logout_B")
el8.click()

driver.quit()