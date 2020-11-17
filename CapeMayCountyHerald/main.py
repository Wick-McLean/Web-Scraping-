from selenium import webdriver

import writeToAws
from getSectionUrls import capeHeraldGetPageUrls
from getArticleText import getArticleText
import time

url = ('https://www.capemaycountyherald.com/opinion/')
driver = webdriver.Chrome('../../PycharmProjects/ArticlesDownloadSave/chromedriver.exe')

urlList = capeHeraldGetPageUrls(driver, url)
print(urlList)
allNews = ""
for aUrl in urlList:
    allNews += getArticleText(driver, aUrl)
todaysNews = open('todaysNews.txt', 'w')
todaysNews.write(allNews)
todaysNews.close()

nameFileCurrentTime = time.strftime("%Y-%m-%d %H:%M:%S.txt")
writeToAws.upload_to_aws('todaysNews.txt', 'nymag-scrape-articles-from-python', nameFileCurrentTime)