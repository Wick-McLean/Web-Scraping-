from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

r = requests.get("http://nymag.com/_components/nymag-latest-feed/instances/index@published")
json=r.json()
urllist=json["manualArticleUrls"]


driverList = []
#for i in range (len(urllist)):
for i in range (2):
    driver = webdriver.Chrome()
    driver.get((urllist[i+4])+"#comments")
    driverList.append(driver)
    linkify=driver.find_element_by_xpath('//*[@id="talk-embed-stream-container"]/div[1]')
    print(linkify)



# for i in range(len(driverList)):
for i in range(2):
    driverList[i].quit()


