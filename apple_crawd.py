# 爬蟲 完整版_20180825v1_20190210v2
from urllib.request import urlopen
from bs4 import BeautifulSoup 

import re
import requests
import time
import random
import pandas as pd
from pandas import DataFrame
import csv

def ad_clear(id):
    try:
        ad87=id
        time.sleep(3)
        browser.find_element_by_xpath(ad87).click()
        time.sleep(2)
    except:
        pass

html = urlopen("https://tw.appledaily.com/new/realtime")
soup = BeautifulSoup(html,'html.parser')

title_list=[]
count=0
local_title_list=[]
local_href_list = []
local_political_title_list = []
local_political_href_list=[]
local_entertainment_title_list=[]
local_entertainment_href_list = []
local_national_title_list=[]
local_national_href_list=[]
local_life_title_list=[]
local_life_href_list=[]






# count = 爬蟲頁數
def app_social_fun():
    global count
    global soup
    global html

    global title_list
    global local_title_list
    global local_href_list 

    global local_national_title_list
    global local_national_href_list

    global local_entertainment_title_list
    global local_entertainment_href_list

    global local_life_title_list
    global local_life_href_list

    
    while count<=1:
        
        #找到title 共有幾篇
        for i in soup.findAll("ul",{'class':'rtddd slvl'}):
            for j in i.findAll('h1'):
                clean = re.compile('<.*?>')
                a=str(re.sub(clean,'',str(j.text))).replace("\u3000","")
                title_list.append(a)
        
        
        #抓每一則新聞的連結 ，href是每則的連結
        title_count=0
        soup = BeautifulSoup(html, 'html.parser')
        for news_list in soup.findAll("li",{'class':'rtddt'}): 
            if title_count < len(title_list): 
                b=str(news_list.h2)
                b = b[4:6]
                if b == "社會":
                    href="https://tw.news."+news_list.a['href'].strip("/")[16:]
                    local_href_list.append(href)
                    html2 = urlopen(href)

                    #去除廣告
                    # ad_clear('//div[@id="tenmax-cover-shrink"]')
                    bsObj = BeautifulSoup(html2, 'html.parser')
                    # print(bsObj)                  
                #    找title ,content丟入list中
                    for i in bsObj.findAll("article"):
                        # print(i)
                        if i.h1 != None:
                            local_title_list.append(i.h1.get_text().replace("\xa0","").replace('\u3000',"").replace("\xa0","").replace("\u200b",""))
                    title_count+=1
                elif b == "政治":
                    href="https://tw.news."+news_list.a['href'].strip("/")[16:]
                    local_political_href_list.append(href)
                    html2 = urlopen(href)

                    #去除廣告
                    # ad_clear('//div[@id="tenmax-cover-shrink"]')
                    bsObj = BeautifulSoup(html2, 'html.parser')
                    # print(bsObj)                  
                #    找title ,content丟入list中
                    for i in bsObj.findAll("article"):
                        # print(i)
                        if i.h1 != None:
                            local_political_title_list.append(i.h1.get_text().replace("\xa0","").replace('\u3000',"").replace("\xa0","").replace("\u200b",""))
                    title_count+=1
                elif b == "國際":
                    href="https://tw.news."+news_list.a['href'].strip("/")[16:]
                    local_national_href_list.append(href)
                    html2 = urlopen(href)

                    #去除廣告
                    # ad_clear('//div[@id="tenmax-cover-shrink"]')
                    bsObj = BeautifulSoup(html2, 'html.parser')
                    # print(bsObj)                  
                #    找title ,content丟入list中
                    for i in bsObj.findAll("article"):
                        # print(i)
                        if i.h1 != None:
                            local_national_title_list.append(i.h1.get_text().replace("\xa0","").replace('\u3000',"").replace("\xa0","").replace("\u200b",""))
                    title_count+=1
                elif b == "娛樂":
                    href="https://tw."+news_list.a['href'].strip("/")[11:]
                    local_entertainment_href_list.append(href)
                    html2 = urlopen(href)

                    #去除廣告
                    # ad_clear('//div[@id="tenmax-cover-shrink"]')
                    bsObj = BeautifulSoup(html2, 'html.parser')
                    # print(bsObj)                  
                #    找title ,content丟入list中
                    for i in bsObj.findAll("article"):
                        # print(i)
                        if i.h1 != None:
                            local_entertainment_title_list.append(i.h1.get_text().replace("\xa0","").replace('\u3000',"").replace("\xa0","").replace("\u200b",""))
                    title_count+=1
                elif b == "生活":
                    href="https://tw.news."+news_list.a['href'].strip("/")[16:]
                    local_life_href_list.append(href)
                    html2 = urlopen(href)

                    #去除廣告
                    # ad_clear('//div[@id="tenmax-cover-shrink"]')
                    bsObj = BeautifulSoup(html2, 'html.parser')
                    # print(bsObj)                  
                #    找title ,content丟入list中
                    for i in bsObj.findAll("article"):
                        # print(i)
                        if i.h1 != None:
                            local_life_title_list.append(i.h1.get_text().replace("\xa0","").replace('\u3000',"").replace("\xa0","").replace("\u200b",""))
                    title_count+=1
            else:#跑完新聞後，回至首頁,跳出迴圈繼續下面。
                break
        html_count=str(count+1)
        html_next = 'https://tw.appledaily.com/new/realtime/'+html_count
        print(html_next)
        html = urlopen(html_next)
        
        
        # print(html_count)
        count+=1
