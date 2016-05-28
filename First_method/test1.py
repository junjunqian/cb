#!/usr/bin/env python
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import csv
import codecs

# Overview(yahoo_html)
def Overview(company_html):
    company_name = "None"
    headquarter = "None"
    brief_description = "None"
    founders = "None"
    categories = "None"
    website = "None"
    overview_detail = []
    soup = BeautifulSoup(company_html.strip(), "html.parser")
    try:
        company_name = str(soup.find("h1", {"id": "profile_header_heading"}).text)
    except:
        company_name = "None"
    try:
        for i in soup.find("div", attrs = {"class" : "definition-list container"}):
            overview_detail.append(str(i.text.encode('ascii', 'ignore')))
        for l in range(len(overview_detail)):
            if "Headquarters:" in overview_detail[l]:
                headquarter = overview_detail[l+1]
            if "Description:" in overview_detail[l]:
                brief_description = overview_detail[l+1]
            if "Founders:" in overview_detail[l]:
                founders = overview_detail[l+1]
            if "Categories:" in overview_detail[l]:
                categories = overview_detail[l+1]
            if "Website:" in overview_detail[l]:
                website = overview_detail[l+1]
    except:
        pass
    return company_name, headquarter, brief_description, founders, categories, website


# company found time, emp number, detail description
# company_details(yahoo_html)
def company_details(company_html):
    found_time = "None"
    employ_num = "None"
    detail_description = "None"
    soup = BeautifulSoup(company_html.strip(), "html.parser")
    soup2 = soup.find("div", attrs = {"class" : "base info-tab description"}).find("div", attrs = {"class" : "card-content box container card-slim"})
    description_list = []
    comp_detail = []
    temp_soup = soup2.find("div", attrs = {"class" : "details definition-list"})
    for i in temp_soup:
        comp_detail.append(i.text)
    for l in range(len(comp_detail)):
        if "Founded:" in comp_detail[l]:
            found_time = str(comp_detail[l+1])
        if "Employees:" in comp_detail[l]:
            employ_num = comp_detail[l+1]
    try:
        for i in soup2.find("div", attrs = {"class" : "description-ellipsis"}).findAll("p"):
            paragraph = str(i.text.encode('ascii', 'ignore'))
            description_list.append(paragraph)
        detail_description = " ".join(description_list)
    except:
        detail_description = "None"
    return found_time, employ_num, detail_description

# ipo_status(yahoo_html)
def ipo_status(company_html):
    ipo_date = "None"
    ipo_symbol = "None"
    ipo_exchange = "None"
    IPO_status = ""
    soup = BeautifulSoup(company_html.strip(), "html.parser")
    try:
        IPO_status = str(soup.find("div", attrs = {"class" : "overview-stats"}).find("dt", text = "IPO / Stock").text.encode('ascii', 'ignore'))
    except:
        pass
    if len(IPO_status) != 0:
        ipo_info = soup.find("div", attrs = {"class" : "overview-stats"}).find("dt", text = "IPO / Stock").find_next_sibling().text # found.find_next_sibling("dd") or found.find_next_sibling("dt")
        ipo_date_raw = str(ipo_info.split("/")[0].split("on ")[1].strip()) # strip to get rid of space at the end
        date_format1 = "%b %d, %Y"
        try:
            ipo_date = datetime.strptime(ipo_date_raw, date_format1).isoformat().split("T")[0]
        except:
            ipo_date = "None"
        try:
            ipo_symbol = str(ipo_info.split("/")[1].split(":")[1])
        except:
            ipo_symbol = "None"
        try:
            ipo_exchange = str(ipo_info.split("/")[1].split(":")[0])        
        except:
            ipo_exchange = "None"
    return ipo_date, ipo_symbol, ipo_exchange

# total funding amount
def total_funding(company_html):
    total_funding = "None"
    soup = BeautifulSoup(company_html.strip(), "html.parser")
    try:
        total_funding = str(soup.find("div", attrs = {"class" : "base info-tab funding_rounds"}).find("h2", attrs = {"class" : "headline", "id" : "funding_rounds"}).text.split("- ")[1])
        if 'k' in total_funding:
            total_funding = total_funding[0]+str(int(float(str(total_funding).split(total_funding[0])[1].split('k')[0]) * 1000))
        elif 'M' in total_funding:
            total_funding = total_funding[0]+str(int(float(str(total_funding).split(total_funding[0])[1].split('M')[0]) * 1000000))
        elif 'B' in total_funding:
            total_funding = total_funding[0]+str(int(float(str(total_funding).split(total_funding[0])[1].split('B')[0]) * 1000000000))
        else:
            total_funding = total_funding[0]+str(0)
    except:
        total_funding = "None"
    return total_funding

# Funding Rounds table
# funding_detail = funding_detail(company_html)
def funding_detail(company_html):
    funding_detail = [["None"]]
    soup = BeautifulSoup(company_html.strip(), "html.parser")
    try:
        funding_detail_c=[]
        for i in soup.find("div", attrs = {"class" : "base info-tab funding_rounds"}).find("div", attrs = {"class" : "card-content box container card-slim"}).find("table", attrs = {"class" : "table container"}).findAll("tr"):
            for l in i:
                funding_detail_c.append(l.text)
        funding_detail=[funding_detail_c[x:x+5] for x in xrange(0, len(funding_detail_c), 5)]
    except:
        funding_detail = [["None"]]
    return funding_detail

# break down the Funding Rounds table: Typle and Amount
# funding_round(yahoo_html)
def funding_round(company_html):
    type_list = []
    amount_list = []
    for i in range(len(funding_detail)):
        try:       
            funding_amount = funding_detail[i][1].split(" / ")[0]
            funding_amount = funding_amount.replace(funding_amount[0],"")#split("$")[1]
            if 'k' in funding_amount:
                funding_amount = int(float(funding_amount.split('k')[0]) * 1000)
            elif 'M' in funding_amount:
                funding_amount = int(float(funding_amount.split('M')[0]) * 1000000)
            elif 'B' in funding_amount:
                funding_amount = int(float(funding_amount.split('B')[0]) * 1000000000)
            else:
                funding_amount = 0
            funding_type = funding_detail[i][1].split(" / ")[1]
        except:
            funding_type = "None"
            funding_amount = 0
            pass
        if funding_type not in type_list:
            type_list.append(str(funding_type))
            amount_list.append(funding_amount)
        else:
            amount_list[-1] = amount_list[-1] + funding_amount
    return type_list, amount_list


# break down the Funding Rounds table: Funding date
def funding_date(company_html):
    try:
        fund_date_list = []
        temp_date_list = []
        date_format = "%b, %Y"
        for i in type_list:
            for l in range(len(funding_detail)):
                if i in funding_detail[l][1]:
                    fund_date = funding_detail[l][0]
                    temp_date = datetime.strptime(fund_date, date_format).isoformat().split("T")[0]
                    temp_date_list.append(temp_date)
            if len(temp_date_list) > 1:
                temp_date_list = [temp_date_list[-1]," to ",temp_date_list[0]]
                str1 = ''.join(temp_date_list)
            else:
                temp_date_list = [temp_date_list[-1]," to ",temp_date_list[0]]
                str1 = ''.join(temp_date_list)
            fund_date_list.append(str1)
            temp_date_list = []
    except:
        fund_date_list = ["None"]
    return fund_date_list

# Investors table
# investor(yahoo_html)
def investor_table(company_html):
    soup = BeautifulSoup(company_html.strip(), "html.parser")
    first_col = []
    second_col = []
    temp_sec = []
    third_col = []
    temp_third = []
    try:
        investor_section = soup.find("div", attrs = {"class" : "base info-tab investors"}).find("table", attrs = {"class" : "table section-list investors"}).findAll("tbody")
        for i in investor_section:
            first_col.append(str(i.find("tr").find("td").find("a").text))
        for l in range(len(investor_section)):
            for result in investor_section[l].findAll("tr"):
                a_section = result.findAll("a")
                for i in a_section:
                    if len(i.attrs) == 1 :
                        temp_sec.append(str(i.text))
            second_col.append(temp_sec)
            temp_sec=[]
        for l in investor_section:
            for i in range(len(l.findAll("tr"))):
                if len(l.findAll("tr")[i].findAll("td")[-1].findAll("div")) == 0:
                    temp_name = l.findAll("tr")[i].findAll("td")[-1].text
                    temp_third.append(str(temp_name))
                else:
                    temp_section = l.findAll("tr")[i].findAll("div")
                    for i in temp_section:
                        temp_name = i.text
                        temp_third.append(str(temp_name))
            third_col.append(temp_third)    
            temp_third = []
    except:
        first_col = ["None"]
        second_col = [["None"]]
        third_col = [["None"]]
    return first_col, second_col, third_col

# break down the Investors table: Investor list for each round
# investor(yahoo_html)
def investor(company_html):
    soup = BeautifulSoup(company_html.strip(), "html.parser")
    result_temp_list = []
    flat_list=[]
    investor_list = []
    for funding_type in type_list:
        for l in range(len(second_col)):
            for j in range(len(second_col[l])):
                if funding_type == second_col[l][j]:
                    if len(second_col[l]) == len(third_col[l]):
                        result_temp_list.append(first_col[l])
                        result_temp_list.append(third_col[l][j])
                    else:
                        result_temp_list.append(first_col[l])
                        result_temp_list.append(third_col[l])
        for i in range(len(result_temp_list)):
            if (type(result_temp_list[i]) == str and result_temp_list[i] != "-"):
                flat_list.append(result_temp_list[i])
            else:
                for l in range(len(result_temp_list[i])):
                    if result_temp_list[i][l] != "-":
                        flat_list.append(result_temp_list[i][l])
        flat_list_str = ', '.join(flat_list)
        investor_list.append(flat_list_str)
        flat_list =[] 
        result_temp_list = []
    return investor_list


#inputfile = "/Users/Junjun/Desktop/google.html"
#inputfile = "/Users/Junjun/Desktop/facebook.html"
#inputfile = "/Users/Junjun/Desktop/omidyarnetwork.html"
#inputfile = "/Users/Junjun/Desktop/wetpaint.html"
#inputfile = "/Users/Junjun/Desktop/accelpartners.html"
#inputfile = "/Users/Junjun/Desktop/geni.html"
#inputfile = "/Users/Junjun/Desktop/omnidrive.html"
#inputfile = "/Users/Junjun/Desktop/zoho.html"
#inputfile = "/Users/Junjun/Desktop/digg.html"
#inputfile = "/Users/Junjun/Desktop/meritechcapitalpartners.html"
#inputfile = "/Users/Junjun/Desktop/trinityventures.html"
inputfile = "/root/html_file/00000.html"
company_html = codecs.open(inputfile, 'r').read()
company_name = Overview(company_html)[0]
if company_name != "None":
    headquarter = Overview(company_html)[1] 
    brief_description = Overview(company_html)[2]
    founders = Overview(company_html)[3]
    categories = Overview(company_html)[4]
    website = Overview(company_html)[5]
    found_time = company_details(company_html)[0]
    employ_num = company_details(company_html)[1]
    detail_description = company_details(company_html)[2]
    ipo_date = ipo_status(company_html)[0]
    ipo_symbol = ipo_status(company_html)[1]
    ipo_exchange = ipo_status(company_html)[2]
    total_funding = total_funding(company_html)
    funding_detail = funding_detail(company_html) # not output
    if funding_detail != [["None"]]:
        type_list = funding_round(company_html)[0] # not output
        amount_list = funding_round(company_html)[1] # not output
        fund_date_list = funding_date(company_html) # not output
        first_col = investor_table(company_html)[0]# not output
        second_col = investor_table(company_html)[1]# not output
        third_col = investor_table(company_html)[2]# not output
        investor_list = investor(company_html)# not output
        zip_list = zip(type_list, amount_list, fund_date_list, investor_list)
        excel_list = []
        for single_result in zip_list:
            for l in range(len(single_result)):
                excel_list.append(single_result[l])
        with open('result.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([company_name] + [headquarter] + [brief_description] + [founders] + [categories] + [website] + [found_time] + [employ_num] + [detail_description] + [ipo_date] + [ipo_symbol] + [ipo_exchange] + [total_funding] + excel_list)
    else:
        with open('result.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([company_name] + [headquarter] + [brief_description] + [founders] + [categories] + [website] + [found_time] + [employ_num] + [detail_description] + [ipo_date] + [ipo_symbol] + [ipo_exchange] + [total_funding])
else:
    print "Wrong Page"
    pass

"""
with open('result.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Company Name"] + ["Headquarter"] + ["Brief Description"] + ["Founders"] + ["Categories"] + ["Website"] + ["Found time"] + ["Employees Number"] + ["Detail Description"] + ["IPO Date"] + ["IPO Symbol"] + ["IPO Exchange"] + ["Total Funding Amount"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"] + ["Funding Round"] + ["Funding Amount"] + ["Funding Date"] + ["Investors"])
"""



