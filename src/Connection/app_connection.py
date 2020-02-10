# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# coding: utf-8

from appium import webdriver


### MurayamaKenta -> ###
caps = {
    "platformName" : "Android",
    "automationName" : "Appium",
    "platformVersion" : "8.0",
    "deviceName" : "Android Emulator",
    "app" : "/Users/murayamakenta/Downloads/test/app-rc.apk",
    "appWaitDuration" : 10000 ,
    "appWaitActivity" : "com.quipper.school.assignment.ui.start.login.LoginActivity",
 }

# caps["platformName"] = "Android"
# caps["automationName"] = "Appium"
# caps["platformVersion"] = "8.0"
# caps["deviceName"] = "Android Emulator"
# caps["app"] = "/Users/murayamakenta/Downloads/test/app-rc.apk"
# caps["appWaitDuration"] = 10000
# caps["appWaitActivity"] = "com.quipper.school.assignment.ui.start.login.LoginActivity"




### <- MurayamaKenta ###

### RyoMoriya -> ###
# caps = {}
# caps["platformName"] = "Android"
# caps["automationName"] = "Appium"
# caps["platformVersion"] = "7.0"
# caps["deviceName"] = "Android Emulator"
# caps["app"] = "/Users/moriyaryou/ApkProjects/app-rc/app-rc.apk"
# caps["appWaitPackage"] = "jp.studysapuri.android.rc"
# caps["appWaitActivity"] = "com.quipper.school.assignment.ui.LoginActivity"
### <- RyoMoriya ###

def driver():
    global caps
    driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
    return driver