import datetime
#Webscraper libraries
import requests
import textwrap
from bs4 import BeautifulSoup
from lxml import html



def main():
    CNNWebScraped = CNNWebscraper()
    makeCSV(CNNWebScraped)

def makeCSV(CNNWebScraped):
    fp = open('CNNstock.csv','w')

    if fp == None:
        print("Error opening file")
        exit(1)
    fp.write("name-code,price,change,percent-change,pe,volume,ytd-change\n")
    for y in range(len(CNNWebScraped)):
        for x in range(len(CNNWebScraped[y]) - 1):
            fp.write(CNNWebScraped[y][x]+",")
        fp.write(CNNWebScraped[y][x + 1]+"\n")
    fp.close()    

def CNNWebscraper():
    company = []
    for i in range(1,90):
        print(i)
        url = "http://money.cnn.com/data/markets/russell/?page={0}".format(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        divClass = soup.find('div',id="wsod_indexConstituents")
        table = divClass.find('div',class_="wsod_dataTableBorder")
        table_body = table.find('tbody')
        rows = table_body.find_all('td')
    
        for i in range(0,len(rows),7):
            name = rows[i]
            try:
                name = name.find('a').text  
            except:
                continue
                
            price = rows[i+1]
            if price == "--":
                continue
            price = price.find('span').text
            change = rows[i+2]
            change = change.find('span').text
            percentChange = rows[i+3]
            percentChange = percentChange.find('span').text
            pe = rows[i+4]
            if pe.text == "--":
                pe = "NA"
            else:
                pe = pe.text
            vol = rows[i+5]
            if vol.text == "--":
                vol = "NA"
            else:
                vol = vol.text
            ytdChange = rows[i+6]
            if ytdChange.text == "--":
                ytdChange = "NA"
            else:
                ytdChange = ytdChange.find('span').text
            company.append([name,price,change,percentChange,pe,vol,ytdChange])

    return company

def yahooTestScraper():
    company = []
    url = "http://money.cnn.com/data/markets/russell/?page={0}".format(1)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    divClass = soup.find('div',id="wsod_indexConstituents")
    table = divClass.find('div',class_="wsod_dataTableBorder")
    table_body = table.find('tbody')
    rows = table_body.find_all('td')
    
    for i in range(0,len(rows),7):
        name = rows[i]
        name = name.find('a').text
        price = rows[i+1]
        price = price.find('span').text
        change = rows[i+2]
        change = change.find('span').text
        percentChange = rows[i+3]
        percentChange = percentChange.find('span').text
        pe = rows[i+4]
        if pe == None:
            pe = "NA"
        else:
            pe = pe.text
        vol = rows[i+5]
        if vol == None:
            vol = "NA"
        else:
            vol = vol.text
        ytdChange = rows[i+6]
        if ytdChange == None:
            ytdChange = "NA"
        else:
            ytdChange = ytdChange.find('span').text
        
        company.append([name,price,change,percentChange,pe,vol,ytdChange])
    for i in range(len(company)):
        print(company)
    return 0
"""
   rows = table_body.find_all('tr')
   for row in rows:
        columns = row.find('td')
        for col in columns:
            print(str(col))
"""




main()