from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import requests
import sys

url= urlopen('https://oursogo.com/forum-42-1.html') 
soup = BeautifulSoup(url,'html.parser')




title_list = []
href_list = []
food_title = ""


def getFoodList():
    for i in soup.findAll('tbody'):
        set_id = i.get('id')
        if(set_id[0:13] == "normalthread_"):
            title_list.append(i.findAll('a')[2].string)
            href_list.append(i.findAll('a')[2].get('href'))
print(title_list)
print(href_list)
