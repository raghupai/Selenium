'''
Created on 18-May-2020

@author: raghuveer
'''

#import the webdriver
from selenium import webdriver
import time

#set exe path and open the chrome browser.
browser = webdriver.Chrome("/usr/local/bin/chromedriver");

#open the google scholar application
browser.get("https://scholar.google.com/");

#maximize the window
browser.maximize_window()

#Fetch the current URL and title of the page and print in the console
print("Current URL of the page : " , browser.current_url)
print("Title of the page :" , browser.title)

#close the browser
browser.close()
