# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["automationName"] = "Appium"
caps["platformVersion"] = "8.0"
caps["deviceName"] = "Android Emulator"
caps["app"] = "/Users/murayamakenta/Downloads/test/app-rc.apk"
caps["appWaitDuration"] = 10000
caps["appWaitActivity"] = "com.quipper.school.assignment.ui.start.login.LoginActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("jp.studysapuri.android.rc:id/username_V")
el1.send_keys("5321")
el2 = driver.find_element_by_id("jp.studysapuri.android.rc:id/password_V")
el2.send_keys("quipper123")
el3 = driver.find_element_by_id("jp.studysapuri.android.rc:id/login_B")
el3.click()

time.sleep(5)
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.RelativeLayout")
el4.click()

time.sleep(3) 
el5 = driver.find_element_by_accessibility_id("講義一覧")
el5.click()
time.sleep(3) 
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout")
el6.click()
time.sleep(3) 
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView")
el7.click()
time.sleep(3) 
el8 = driver.find_element_by_accessibility_id("上へ移動")
el8.click()
time.sleep(3) 
el9 = driver.find_element_by_accessibility_id("上へ移動")
el9.click()
time.sleep(3) 
el10 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"icon\"])[2]")
el10.click()


# time.sleep(3) 
# el11 = driver.find_element_by_accessibility_id("ダウンロード済")
# el11.click()
# time.sleep(3) 
# el12 = driver.find_element_by_id("jp.studysapuri.android.rc:id/course_container_V")
# el12.click()
# time.sleep(3) 
# el13 = driver.find_element_by_accessibility_id("再生")
# el13.click()
# time.sleep(5) 

# el14 = driver.find_element_by_accessibility_id("上へ移動")
# el14.click()
# time.sleep(3) 
# el15 = driver.find_element_by_accessibility_id("上へ移動")
# el15.click()

# driver.quit()