#!/usr/bin/env python
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import codecs
import csv as csv
import random
import time 
import json
import sys
import re

# 05 to 15, bayarea, california, find html page for all.

first_arg = sys.argv[1]
second_arg = sys.argv[2]
third_arg = sys.argv[3]
fourth_arg = sys.argv[4]

'''
city_name='San'
state_name='California'
city_n = ' '.join(re.findall('[A-Z][^A-Z]*', city_name))
city_state = city_n + ", " + state_name
'''

def found(after=first_arg, before=second_arg, city_name=third_arg, state_name=fourth_arg):
    a2 = str(after[2:4])
    b2 = str(before[2:4])
    output_file = a2 + b2 + city_name + str('.txt')
    city_n = ' '.join(re.findall('[A-Z][^A-Z]*', city_name))
    city_state = city_n + ", " + state_name
    companyname_list = []
    display = Display(visible=0, size=(1024, 768))
    display.start()
    browser = webdriver.Firefox()
    time.sleep(randint(20,40))
    browser.get("https://www.crunchbase.com/search")
    time.sleep(randint(25,35))
    if after == "2015":
        a =  '//*[@id="founded_after"]/option[2]'
    elif after == "2014":
        a =  '//*[@id="founded_after"]/option[3]'
    elif after == "2013":
        a =  '//*[@id="founded_after"]/option[4]'
    elif after == "2012":
        a =  '//*[@id="founded_after"]/option[5]'
    elif after == "2011":
        a =  '//*[@id="founded_after"]/option[6]'
    elif after == "2010":
        a =  '//*[@id="founded_after"]/option[7]'
    elif after == "2009":
        a =  '//*[@id="founded_after"]/option[8]'
    elif after == "2008":
        a =  '//*[@id="founded_after"]/option[9]'
    elif after == "2007":
        a =  '//*[@id="founded_after"]/option[10]'
    elif after == "2006":
        a =  '//*[@id="founded_after"]/option[11]'
    elif after == "2005":
        a =  '//*[@id="founded_after"]/option[12]'
    time.sleep(2)    
    if before == "2015" and after == "2015":
        b =  '//*[@id="founded_before"]/option[1]'
    elif before == "2015":
        b =  '//*[@id="founded_before"]/option[2]'
    elif before == "2014":
        b =  '//*[@id="founded_before"]/option[3]'
    elif before == "2013":
        b =  '//*[@id="founded_before"]/option[4]'
    elif before == "2012":
        b =  '//*[@id="founded_before"]/option[5]'
    elif before == "2011":
        b =  '//*[@id="founded_before"]/option[6]'
    elif before == "2010":
        b =  '//*[@id="founded_before"]/option[7]'
    elif before == "2009":
        b =  '//*[@id="founded_before"]/option[8]'
    elif before == "2008":
        b =  '//*[@id="founded_before"]/option[9]'
    elif before == "2007":
        b =  '//*[@id="founded_before"]/option[10]'
    elif before == "2006":
        b =  '//*[@id="founded_before"]/option[11]'
    elif before == "2005":
        b =  '//*[@id="founded_before"]/option[12]'
    browser.find_element(By.XPATH, a).click()
    time.sleep(randint(65,75))
    browser.find_element(By.XPATH, b).click()
    time.sleep(randint(15,25))
    search = browser.find_element_by_name('location_input')
    time.sleep(randint(2,3))
    search.send_keys(city_state)
    time.sleep(randint(5,7))
    browser.find_element(By.XPATH, '//*[@id="ui-id-2"]/li[1]').click()
    time.sleep(randint(5,7))
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    n = 0
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(randint(25,35))
        newHeight = browser.execute_script("return document.body.scrollHeight")
        n = n + 1
        if n == 50:
            time.sleep(randint(5,10))
            n = 0
            cn_a = browser.page_source
            with open(output_file,'w') as myfile:
                json.dump(cn_a,myfile)
            #print (cn_a)
        print (n)
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
    time.sleep(randint(15,25))
    cn_a = browser.page_source
    time.sleep(randint(55,60))
    browser.quit()
    display.stop()
    with open(output_file,'w') as myfile:
        json.dump(cn_a,myfile)
    return cn_a


print ('Done read fundtion')
#foundyear = found('2015','2015')


if __name__ == "__main__":
    foundyear = found()
