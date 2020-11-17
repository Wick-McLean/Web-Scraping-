import requests
from bs4 import BeautifulSoup

#return list of urls
def njStarLinks():
    njUrl = 'https://www.newjerseyhills.com/search/?f=rss&t=article&c=bernardsville_news&l=50&s=start_time&sd=desc'
    r = requests.get(njUrl).text
    soup = BeautifulSoup(r, "html.parser")
    allLoc = soup.find_all('link')
    print(allLoc)



    # print(soup.prettify())

getnymaglinks()

#Run this only if user manually says to run it
# if __name__ == "__main__":
#     print(getnymaglinks())
    # r=requests.get('http://nymag.com/intelligencer/2020/01/sanders-campaign-goes-negative-on-warren-in-volunteer-script.html#comments')
    # print(r.text)