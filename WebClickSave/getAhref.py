from bs4 import BeautifulSoup
import requests
import lxml

#returns a list of all a href links from a webpage
def returnLinkList(webPage):

    html = requests.get(webPage)
    soup = BeautifulSoup(html.text, 'lxml')
    linkList = []
    for link in soup.findAll('a'):
        linkList.append(link.get('href'))
    # endgame = linkList.json()
    # print(endgame)
    print(linkList)
    print (len(linkList))

returnLinkList('https://nypost.com/')