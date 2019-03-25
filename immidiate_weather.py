#coding=UTF-8 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import requests
import sys

# 今日白天
title = ""
weather_time = ""
weather_temperature = ""
weather_situation = "" 
weather_feel = ""
weather_rain = ""

#今晚至明晨
weather_tonight_time = ""
weather_tonight_temperature = ""
weather_tonight_situation = ""
weather_tonight_feel = ""
weather_tonight_rain = ""


#明日白天
weather_tomorrow_time = ""
weather_tomorrow_temperature = ""
weather_tomorrow_situation = ""
weather_tomorrow_feel = ""
weather_tomorrow_rain = ""

def search(new_url):
    global title
    global weather_time
    global weather_temperature
    global weather_situation
    global weather_feel
    global weather_rain
    global weather_tonight_time
    global weather_tonight_temperature
    global weather_tonight_situation
    global weather_tonight_feel
    global weather_tonight_rain
    global weather_tomorrow_time
    global weather_tomorrow_temperature
    global weather_tomorrow_situation
    global weather_tomorrow_feel
    global weather_tomorrow_rain
    url= urlopen(new_url) 
    soup = BeautifulSoup(url,'html.parser')
    title = soup.findAll(id='box8')[0].findAll('tr')[0].findAll('th')[0].string
    print(title)
    # total_data = soup.findAll('tr')[1]
    
    #今日白天
    weather_time = soup.findAll(id='box8')[0].findAll('tr')[1].findAll('th')[0].string
    print('時間'+weather_time)
    weather_temperature = soup.findAll(id='box8')[0].findAll('tr')[1].findAll('td')[0].string
    weather_situation = soup.findAll(id='box8')[0].findAll('tr')[1].findAll('td')[1].findAll('img')[0].get('alt')
    weather_feel = temperature = soup.findAll(id='box8')[0].findAll('tr')[1].findAll('td')[2].string
    weather_rain = temperature = soup.findAll(id='box8')[0].findAll('tr')[1].findAll('td')[3].string
    print('溫度'+weather_temperature)
    print('天氣狀況'+weather_situation)
    print('舒適度'+weather_feel)
    print('降雨機率 (%)  '+weather_rain)
    print ('\n')
    #今晚至明晨
    weather_tonight_time = soup.findAll(id='box8')[0].findAll('tr')[2].findAll('th')[0].string
    print('時間'+weather_tonight_time)
    weather_tonight_temperature = soup.findAll(id='box8')[0].findAll('tr')[2].findAll('td')[0].string
    weather_tonight_situation = soup.findAll(id='box8')[0].findAll('tr')[2].findAll('td')[1].findAll('img')[0].get('alt')
    weather_tonight_feel = temperature = soup.findAll(id='box8')[0].findAll('tr')[2].findAll('td')[2].string
    weather_tonight_rain = temperature = soup.findAll(id='box8')[0].findAll('tr')[2].findAll('td')[3].string
    print('溫度'+weather_tonight_temperature)
    print('天氣狀況'+weather_tonight_situation)
    print('舒適度'+weather_tonight_feel)
    print('降雨機率 (%)  '+weather_tonight_rain)
    print ('\n')
    
    #明日白天
    weather_tomorrow_time = soup.findAll(id='box8')[0].findAll('tr')[3].findAll('th')[0].string
    print('時間'+weather_tomorrow_time)
    weather_tomorrow_temperature = soup.findAll(id='box8')[0].findAll('tr')[3].findAll('td')[0].string
    weather_tomorrow_situation = soup.findAll(id='box8')[0].findAll('tr')[3].findAll('td')[1].findAll('img')[0].get('alt')
    weather_tomorrow_feel = temperature = soup.findAll(id='box8')[0].findAll('tr')[3].findAll('td')[2].string
    weather_tomorrow_rain = temperature = soup.findAll(id='box8')[0].findAll('tr')[3].findAll('td')[3].string
    print('溫度'+weather_tomorrow_temperature)
    print('天氣狀況'+weather_tomorrow_situation)
    print('舒適度'+weather_tomorrow_feel)
    print('降雨機率 (%)  '+weather_tomorrow_rain)


def city(city):
    url= urlopen('http://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm') 
    soup = BeautifulSoup(url,'html.parser')
    for i in soup.findAll("option"):
        if(i.string == city):
            city = i.get('value').split('.')[0]
    if city!=None:
        new_url='http://www.cwb.gov.tw/V7/forecast/taiwan/'+city+'.htm'
        search(new_url)
    else:
        print (u'輸入錯誤')

    print ('\n')