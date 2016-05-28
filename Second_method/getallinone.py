#!/usr/bin/env python
from random import randint
from bs4 import BeautifulSoup
from itertools import product
from csv import DictReader
from pyvirtualdisplay import Display
import codecs
import re
import csv as csv
import itertools
import random
import requests
import time
import json 
import pandas as pd


def get_main(company_html):
    #soup = BeautifulSoup(company_html, 'html.parser')
    inputfile = str("htmlcode/") + company_html
    f = codecs.open(inputfile, 'r')
    soup = BeautifulSoup(f.read())
    company_name = soup.findAll('h1', { "id" : "profile_header_heading"})[0].find(text=True)
    try:
        headquarters = soup.findAll('a', {"href": re.compile(r'/location/.*')})[0].find(text=True)
    except:
        headquarters = 'N/A'
    try:
        category = ', '.join([i.find(text=True) for i in soup.findAll('a', {"href": re.compile(r'/category/.*')})])
    except:
        category = 'N/A'
    try:
        company_website = soup.find(text='Website:').next.find(text=True)
    except:
        company_website = 'N/A'
    try:
        description = soup.find(text='Description:').next.find(text=True) 
    except:
        description = 'N/A'
    try:
        company_description = ' '.join([i.find(text=True) for i in soup.findAll('div', { "class" : "description-ellipsis"})[0].findAll('p')])
    except:
        company_description = 'N/A'
    try:
        founder = ', '.join([i.find(text=True) for i in soup.findAll('div', { "class" : "definition-list container"})[0].findAll('a', {"href": re.compile(r'/person/.*')})])
    except:
        founder = 'N/A'
    try:
        founded_date = str(soup.find('div', { "class" : "details definition-list"}).find('dd').find(text=True))
    except:
        founded_date = 'N/A'
    try:
        number_of_funding_round = int(''.join(re.findall('\d', soup.findAll("span", { "class" : "collection-count"})[1].find(text=True).split('(')[-1].split(')')[0])))
    except:
        number_of_funding_round = 'N/A'
    try:
        total_funding_amount = soup.find('h2', { "id" : "funding_rounds"}).find(text=re.compile('\d[a-zA-Z]$')).split('$')[-1]
        if 'K' in total_funding_amount:
            total_funding_amount = float(total_funding_amount.split('K')[0]) * 1000
        if 'k' in total_funding_amount:
            total_funding_amount = float(total_funding_amount.split('k')[0]) * 1000
        elif 'M' in total_funding_amount:
            total_funding_amount = float(total_funding_amount.split('M')[0]) * 1000000
        elif 'B' in total_funding_amount:
            total_funding_amount = float(total_funding_amount.split('B')[0]) * 1000000000
    except:
        total_funding_amount = 'N/A'
    return company_name, headquarters, category, company_website, description, company_description, founder, founded_date, number_of_funding_round, total_funding_amount



def get_detail(company_html):
    #soup = BeautifulSoup(company_html, 'html.parser')
    #soup = BeautifulSoup(html_list[2])
    inputfile = str("htmlcode/") + company_html
    print (inputfile)
    f = codecs.open(inputfile, 'r')
    soup = BeautifulSoup(f.read())
    funding_round_list = soup.findAll('div', {"class": 'base info-tab funding_rounds'})
    f_r_l = funding_round_list[0].findAll('table', {"class": 'table container'})
    f_r_l2 = f_r_l[0].findAll('tbody')        
    f_r_l1 = f_r_l2[0].findAll('tr')
    funding_detail = []
    for i in range(len(f_r_l1)):
        try:
            funding_d = f_r_l1[i].findAll(text=True)[0]
        except:
            funding_d = 'N/A'            
        funding_detail.append(funding_d)
        try:
            funding_a = f_r_l1[i].findAll(text=True)[1].split(' /')[0].split('$')[-1]
            if 'K' in funding_a:
                funding_a = float(funding_a.split('K')[0]) * 1000
            elif 'k' in funding_a:
                funding_a = float(funding_a.split('k')[0]) * 1000
            elif 'M' in funding_a:
                funding_a = float(funding_a.split('M')[0]) * 1000000
            elif 'B' in funding_a:
                funding_a = float(funding_a.split('B')[0]) * 1000000000
        except:
            funding_a = 'N/A'
        funding_detail.append(funding_a)
        try:
            funding_r = f_r_l1[i].findAll(text=True)[2]
        except:
            funding_r = 'N/A'            
        funding_detail.append(funding_r)
        try:
            funding_v = f_r_l1[i].findAll(text=True)[3]
            if funding_v == '—':
                funding_v = 'N/A'    
        except:
            funding_v = 'N/A'
        funding_detail.append(funding_v)
        try:
            funding_l = f_r_l1[0].findAll('div', {"class": 'link_container'})
            funding_li = ', '.join([i.find(text=True) for i in funding_l])
            if funding_li == "":
                funding_li = 'N/A'
        except:
            funding_li = 'N/A'
        #tmp = []
        #tmp.append(funding_li)
        funding_detail.append(funding_li)
        try:
            funding_in = int(f_r_l1[0].findAll('td', {"class": 'center'})[0].find(text=True))
        except:
            funding_in = 'N/A'
        funding_detail.append(funding_in)
    return funding_detail



def get_error(company_html):
    #soup = BeautifulSoup(company_html, 'html.parser')
    inputfile = str("htmlcode/") + company_html
    f = codecs.open(inputfile, 'r')
    soup = BeautifulSoup(f.read())
    company_name = soup.findAll('h1', { "id" : "profile_header_heading"})[0].find(text=True)
    return company_name



print ("done reading file")


with open('htmlcode/0515list.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Company"] + ["Headquarters"] + ["Category"] + ["Company Website"] + ["Description"] + ["Company Detail"] + ["Founder"] + ["Founded Date"] + ["# of Funding Round"] + ["Total Funding Amount"] + ["Funding Dates"] + ["Funding Amounts"] + ["Rounds"] + ["Valuations"] + ["Lead Investors"] + ["# of Investors"] + ["Funding Dates"] + ["Funding Amounts"] + ["Rounds"] + ["Valuations"] + ["Lead Investors"] + ["# of Investors"] + ["Funding Dates"] + ["Funding Amounts"] + ["Rounds"] + ["Valuations"] + ["Lead Investors"] + ["# of Investors"] + ["Funding Dates"] + ["Funding Amounts"] + ["Rounds"] + ["Valuations"] + ["Lead Investors"] + ["# of Investors"] + ["Funding Dates"] + ["Funding Amounts"] + ["Rounds"] + ["Valuations"] + ["Lead Investors"] + ["# of Investors"])



fobj = open("smallname/smallname_aa.txt","r")
namestring = fobj.read()
namelist = namestring.replace('""','","')
namelist = namelist.replace('"','')
namelist2 = namelist.split(",")
with open('csvoutput/0515list.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    try:
        for i in range(len(namelist2)):
            try:
                final_result = get_main(namelist2[i]) + tuple(get_detail(namelist2[i]))
                writer.writerow(final_result)    
            except:
                final_result = get_main(namelist2[i])
                writer.writerow(final_result)
    except:
        print (namelist2[i])



"""
fobj = open("smallname/smallname_aa.txt","r")
namestring = fobj.read()
namelist = namestring.replace('""','","')
namelist = namelist.replace('"','')
namelist2 = namelist.split(",")
with open('csvoutput/0515list.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    try:
        for i in range(len(namelist2)):
            try:
                final_result = get_main(namelist2[i]) + tuple(get_detail(namelist2[i]))
                writer.writerow(final_result)    
            except:
                final_result = get_main(namelist2[i])
                writer.writerow(final_result)
    except:
        pass
"""
