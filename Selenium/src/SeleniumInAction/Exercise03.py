'''
Created on 11-Jul-2020

@author: raghuveer
'''

#import the webdriver
from selenium import webdriver
#import the locator By
from selenium.webdriver.common.by import By

#set exe path and open the chrome browser.
browser = webdriver.Chrome("/usr/local/bin/chromedriver");

#open the Pack & Go application
browser.get("http://localhost/Automation/PackAndGo_v2/");

#alternatively the above steps can be combined into a single step through method chaining.
browser.find_element_by_link_text("Login").click()

#close the browser
browser.close()
