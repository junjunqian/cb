#!/usr/bin/env python
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
import codecs
import itertools
import random
import time
import sys
import json


first_arg = sys.argv[1]


def openurl(companyname=first_arg):
    display = Display(visible=0, size=(1024, 768))
    display.start()
    browser = webdriver.Firefox()
    time.sleep(randint(8,10))
    try:
        browser.get('http://www.google.com')
        time.sleep(5)
        search = browser.find_element_by_name('q')
        input_text = companyname + str(" crunchbase")
        search.send_keys(input_text)
        time.sleep(randint(10,15))
        search.send_keys(Keys.RETURN)
        time.sleep(randint(10,15))
        gn = browser.find_element_by_tag_name('h3').text
        gnc = str(gn).split(' | ')[0].replace(" ","")
        output_file = '0515' + gnc + '.html'
        browser.find_element_by_link_text(gn).click()
        time.sleep(randint(55,60))
        company_html = browser.page_source
        time.sleep(randint(5,10))
        with open("smallname.txt", 'a') as myfile:
            json.dump(output_file,myfile)
        with open(output_file, 'a+') as myfile:
            myfile.write(company_html)
    except:
        company_html = 'none'        
        with open("missedname.txt", "a") as myfile:
            json.dump(companyname,myfile)            
    time.sleep(1)
    browser.close()
    time.sleep(1)
    display.stop()
    return company_html
    

print ('done read function')


if __name__ == "__main__":
    geturl = openurl()

print (geturl)


"""
lst = 'blabla10something'
# Open the file with a context manager
with open("abc.html", "a+") as myfile:
    # Convert all of the items in lst to strings (for str.join)
    lst = map(str, lst)  
    # Join the items together with commas                   
    line = ",".join(lst)
    # Write to the file
    myfile.write(line)
"""
