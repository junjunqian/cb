#!/usr/bin/env python
from bs4 import BeautifulSoup
from csv import DictReader
import csv as csv
import json
import sys
import re
import itertools

first_arg = sys.argv[1]

# run on local machine
# take the txt file that contain html, read the company name, outpu is a csv file with company name
def convertname(company_html_file=first_arg):
    company_html_file1 = str("result/") + company_html_file
    with open(company_html_file1,'r') as infile:
        company_html = json.load(infile)
    company_name_list=[]
    company_url_list=[]
    soup = BeautifulSoup(company_html)
    soup2 = soup.findAll("div",{"class":"results container"})[0].findAll('ul')[0]
    company_li = soup2.findAll("li")
    for i in range(len(company_li)):
        company_name = company_li[i].findAll("div",{"class":"name follow_card"})[0].find(text=True)
        company_name_list.append(company_name)
        company_url = "www.crunchbase.com" + company_li[i].findAll('a')[0].get('href') + "#/entity"
        company_url_list.append(company_url)
    funding_details = [company_url_list, company_name_list]
    investors_details = list(zip(*funding_details))
    investors_details = list(set(investors_details))
    with open("result/0515output_name.csv", 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for val in investors_details:
            writer.writerow([val][0])
    return investors_details


print ('Done read fundtion')


if __name__ == "__main__":
    convertname = convertname()
