#!/usr/bin/env python
from time import sleep
from random import randint
from googlesearch import GoogleSearch # need to install first
from pprint import pprint
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string 
import datetime
import requests
import csv
import codecs
import sys

# python2.7 comp_html.py https://www.crunchbase.com/organization/io#/entity real

first_arg = sys.argv[1] # https://www.crunchbase.com/organization/io#/entity
second_arg = sys.argv[2] # url_status


def sele_bing(company_url=first_arg):
    pyway = 'sele_bing'
    try:
        display = Display(visible=0, size=(1024, 768))
        display.start()
        print 'display start'
        sleep(randint(1,2))
        online_status = 'online'
    except:
        online_status = 'offline'
        pass
    company_name = company_url.split("/")[-2].split("#")[0]
    exclude = set(string.punctuation)
    company_name = ''.join(ch for ch in company_name if ch not in exclude)
    company_name = company_name.replace(" ","_") # set company_name
    browser = webdriver.Firefox() # open browser
    print 'browser opend'
    sleep(randint(1,2))
    search_url = 'http://www.bing.com/search?q=' + company_url.split("#/entity")[0].replace("/","%2F").replace(":","%3A") # set search_url
    print search_url
    try:
        browser.get(search_url) # use firefox to open search_url
        print 'get search_url done'
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.c_tlbxTrg')))
        sleep(randint(5,10))
        button_click = browser.find_element_by_css_selector('span.c_tlbxTrg')
        button_click.click()
        print 'click button'
        sleep(randint(3,5))
        bing_html1 = browser.page_source
        sleep(randint(5,10))
        soup = BeautifulSoup(bing_html1, "html.parser")
        print soup
        cached_url = soup.find('a', text='Cached page')['href']
        print cached_url
        result_status = "Done"
        print 'Try Success!'
    except:
        cached_url = company_url
        company_html = "Porbably Bing Blocked"
        result_status = "Failed"
        print 'Except Success...'
    finally:
        sleep(randint(3,5))
        browser.quit()
        print 'Browser closed'
        if online_status == 'online':
            sleep(randint(1,2))
            display.stop()
            try:
                bing_html = requests.get(cached_url).text
                company_html = BeautifulSoup(bing_html, "html.parser")
                print 'company_html done'
                print company_html
            except:
                company_html = "Porbably Google Blocked"
                print 'second except failed'
        else:
            pass
    return company_name, company_html, cached_url, result_status, online_status, pyway


if __name__ == "__main__":
    S_NOW = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    co_html = sele_bing()
    if "real" in second_arg:
        S_END = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        if co_html[4] == 'online':
            if co_html[3] == 'Done':
                Html_file1= open("/root/html_file/"+ "00000" + ".html","w")
                Html_file1.write(co_html[1].encode("UTF-8"))
                Html_file1.close()
            else:
                pass
            with open("done_url.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerows([[co_html[0],co_html[2],co_html[3],str(int(S_END)-int(S_NOW)),co_html[5]]])
        else:
            if co_html[3] == 'Done':
                Html_file= open(co_html[0] + ".html","w") # html name
                Html_file.write(co_html[1].encode("UTF-8")) # write html into file
                Html_file.close()
                Html_file1= open("/root/html_file/"+ "00000" + ".html","w")
                Html_file1.write(co_html[1].encode("UTF-8"))
                Html_file1.close()
            else:
                pass
            with open("done_url.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerows([[co_html[0],co_html[2],co_html[3],str(int(S_END)-int(S_NOW)),co_html[5]]]) # wirte note in csv
    else:
        print 'Not real url'
        pass



