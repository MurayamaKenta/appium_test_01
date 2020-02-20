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

# -----login-----
# el3 = driver.find_element_by_id("jp.studysapuri.android.rc:id/username_V")
# el3.send_keys("6901")
# el4 = driver.find_element_by_id("jp.studysapuri.android.rc:id/password_V")
# el4.send_keys("quipper123")
# el5 = driver.find_element_by_id("jp.studysapuri.android.rc:id/login_B")
# el5.click()
# -----login-----


# -----transition profile-----
# el6 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"icon\"])[5]")
# el6.click()
# el7 = driver.find_element_by_accessibility_id("プロフィール")
# el7.click()
# -----transition profile-----


TouchAction(driver)   .press(x=509, y=2026)   .move_to(x=540, y=192)   .release()   .perform()
    
TouchAction(driver)   .press(x=531, y=2013)   .move_to(x=522, y=232)   .release()   .perform()
    

el8 = driver.find_element_by_id("jp.studysapuri.android.rc:id/logout_TV")
el8.click()
el9 = driver.find_element_by_id("jp.studysapuri.android.rc:id/logout_B")
el9.click()

driver.quit()