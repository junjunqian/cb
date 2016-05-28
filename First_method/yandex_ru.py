#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
# company_url = 'https://www.crunchbase.com/organization/roxolar#/entity'   # no search

first_arg = sys.argv[1] # company_url = 'https://www.crunchbase.com/organization/facebook#/entity'
second_arg = sys.argv[2] # url_status


def yandex_ru(company_url=first_arg):
    pyway = 'yandex_ru'
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
    browser = webdriver.Firefox()
    print 'open browser'
    sleep(randint(1,2))
    search_bar = company_url.split("#")[0].split("www.")[1].replace("/o"," > o").replace(" ","%20").replace(">","%3E" ).replace("/","%2F")
    search_url = 'https://yandex.ru/search/?text=' + search_bar + '&lr=200'
    print search_url
    try:
        browser.get(search_url) # use firefox to open search_url
        sleep(randint(5,10))
        yandex_html1 = browser.page_source
        sleep(randint(5,10))
        print 'yandex_html1'
        soup = BeautifulSoup(yandex_html1, "html.parser")
        print soup
        try:
            cached_url = soup.find('a', text = 'Сохранённая копия')['href']
            search_status = 'yes'
            result_status = "Done"
            print cached_url
            print 'Try Success!'
        except:
            cached_url = soup.find('div', text = 'По вашему запросу ничего не нашлось').text
            search_status = 'no'
            result_status = "Failed"
            print cached_url
            print 'Except Success...'
        print 'cached_url: '+ cached_url
        sleep(randint(5,10))
    except:
        cached_url = company_url
        result_status = "Failed"
        search_status = 'no'
        print 'Except 2 Success...'
    finally:
        sleep(randint(3,5))
        browser.quit()
        print 'Browser closed'
        if online_status == 'online':
            sleep(randint(1,2))
            display.stop()
            print search_status
            if (search_status == 'yes' and len(cached_url) > 5):
                yandex_html = requests.get(cached_url).text
                company_html = BeautifulSoup(yandex_html, "html.parser")
                result_status = "Done"
                print 'requests Success'
            else:
                company_html = "Porbably yandex Blocked"
                cached_url = "NotFound"
                result_status = "Failed"
                print 'requests Failed'
            print company_html
            print 'yandex company_html done'                     
        else:
            pass
    return company_name, company_html, cached_url, result_status, online_status, pyway



if __name__ == "__main__":
    S_NOW = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    co_html = yandex_ru()
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
                Html_file= open("/root/html_file/"+co_html[0] + ".html","w")
                Html_file.write(co_html[1].encode("UTF-8"))
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



'''
                Html_file= open("/root/html_file/"+co_html[0] + ".html","w")
                Html_file.write(co_html[1].encode("UTF-8"))
                Html_file.close()
'''
