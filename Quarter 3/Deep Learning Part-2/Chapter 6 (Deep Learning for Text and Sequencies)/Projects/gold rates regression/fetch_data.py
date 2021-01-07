def get_latest_data(num=5):
    
    import requests
    from pprint import pprint 
    from html_table_parser import HTMLTableParser 
    import pandas as pd 
    import numpy as np
    import csv
    from bs4 import BeautifulSoup as bs
    import time
    
    def latest_year():
    
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        link = "https://www.usagold.com/reference/prices/goldhistory.php"

        source = requests.get(link, headers=headers).text
        soup = bs(source,"html.parser")

        l = []
        for li in soup.find("ul", attrs={'id':'goldpriceyearlinks'}):
            li = li.find('a')
            l.append(li)
        l2 = []
        for i in range(0,len(l)-1,2):
            l2.append(l[i-1])
        l = l2[1::]
        links, years = [], []
        for i in l:
            years.append(i.getText())
            links.append(i["href"])

        return links
    
    def scrape_table(url):
    
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        xhtml = requests.get(url, headers=headers).text

        p = HTMLTableParser()
        p.feed(xhtml) 

        table = p.tables[0][2::]
        return p
    
    print("Fetching data......\n")
    
    current_year = latest_year()[0]
    new = scrape_table(current_year)
    
    array = new.tables[0][2:2+int(num)]
    main_list = []
    for i in range(len(array)):
        main_list.append(float(array[i][1]))
        date = str(array[i][0]).replace(" ","-")
        print(f"{date} : {float(array[i][1])}")
    print()
    return main_list