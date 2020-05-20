'''
Created on 18-May-2020

@author: raghuveer
'''

from selenium import webdriver
import time

#set exe path and open the chrome browser.
browser = webdriver.Chrome("/usr/local/bin/chromedriver");

#open the google scholar application
browser.get("https://scholar.google.com/");

#maximize the window
browser.maximize_window()
time.sleep(3)

#Take the screenshot and save as "teller.png"
browser.get_screenshot_as_file("/Users/raghuveer/desktop/Python/image1.png")
time.sleep(3)

#Refresh the page and fetch the page source properties.
browser.refresh()
print("Current URL of the page : " , browser.current_url)
print("Title of the page :" , browser.title)

#close the browser
browser.close()
