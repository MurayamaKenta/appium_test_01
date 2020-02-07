# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# coding: utf-8

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from Connection import app_connection

driver = app_connection.driver()

# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# ダウンロードしてからスリープを入れないと読み込む前に動作してしまいエラーになる
time.sleep(7) 
el2 = driver.find_element_by_id("jp.studysapuri.android:id/username_V")
el2.send_keys("gengoro4")

el3 = driver.find_element_by_id("jp.studysapuri.android:id/password_V")
el3.send_keys("quipper123")

time.sleep(1)
el4 = driver.find_element_by_id("jp.studysapuri.android:id/login_B")
el4.click()

time.sleep(3)
driver.quit()