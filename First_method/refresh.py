#!/usr/bin/env python
from time import sleep
from random import randint
import csv
import codecs

with open('result.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Company Name"] + ["Headquarter"] + ["Brief Description"] + ["Founders"] + ["Categories"] + ["Website"] + ["Found time"] + ["Employees Number"] + ["Detail Description"] + ["IPO Date"] + ["IPO Symbol"] + ["IPO Exchange"] + ["Total Funding Amount"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"])
