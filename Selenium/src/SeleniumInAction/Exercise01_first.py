'''
Created on 29-May-2020

@author: raghuveer
'''

from selenium import webdriver

browser = webdriver.Chrome("/usr/local/bin/chromedriver");

browser.get("http://www.google.com")

browser.close()