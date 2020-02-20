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
# el1 = driver.find_element_by_id("jp.studysapuri.android.rc:id/username_V")
# el1.send_keys("1990")
# el2 = driver.find_element_by_id("jp.studysapuri.android.rc:id/password_V")
# el2.send_keys("quipper123")
# el3 = driver.find_element_by_id("jp.studysapuri.android.rc:id/login_B")
# el3.click()
# -----login-----


# -----プロフィール画面遷移-----
# el4 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"icon\"])[5]")
# el4.click()
# el5 = driver.find_element_by_accessibility_id("プロフィール")
# el5.click()
# -----プロフィール画面遷移-----


# ↓ importが必要。何をするべきなのか調べる
TouchAction(driver)   .press(x=504, y=1999)   .move_to(x=571, y=411)   .release()   .perform()
    
TouchAction(driver)   .press(x=500, y=2022)   .move_to(x=536, y=402)   .release()   .perform()
    
TouchAction(driver)   .press(x=500, y=2017)   .move_to(x=509, y=406)   .release()   .perform()
    
    
el6 = driver.find_element_by_id("jp.studysapuri.android.rc:id/logout_TV")
el6.click()
el7 = driver.find_element_by_id("jp.studysapuri.android.rc:id/logout_B")
el7.click()

driver.quit()