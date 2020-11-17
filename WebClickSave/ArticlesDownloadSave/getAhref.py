from bs4 import BeautifulSoup
import requests
import json


def getAhref(url):
    parser = 'lxml'
    nypost = requests.get(url)
    soup = BeautifulSoup(nypost.text, parser)
    list = []
    for link in soup.findAll('a'):
        finals = (link.get('href'))
        list.append(finals + '\n')
    str1 = ''.join(list)
    print(str1)
    return str

getAhref(url)