from urlManager import getUrls
from nextBottomButtonClick import clickNext
from selenium import webdriver
from openPage import driverOpenPage
import urlManager

driver = webdriver.Chrome('chromedriver.exe')
url = ('https://www.fmprc.gov.cn/mfa_eng/wjdt_665385/zyjh_665391/')

driverOpenPage(driver, url)
getUrls(driver, url)
clickNext(driver)
    while clickNext() is True:

driver.close()
