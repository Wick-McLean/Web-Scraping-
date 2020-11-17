from selenium import webdriver
import json

driver = webdriver.Chrome()

def getSpeechUrls():
    driver.get("https://www.fmprc.gov.cn/mfa_eng/wjdt_665385/zyjh_665391/")
    elem = driver.find_element_by_class_name('newsLst_mod')
    speechUrls = [x.get_attribute('href') for x in elem.find_elements_by_css_selector('a')]
    driver.close()
    return speechUrls

def removeDuplicateUrls(speechUrls):
    with open('masterUrls.txt', 'r') as masterUrlListFile:
        listFile = list(masterUrlListFile)
    masterUrlListFile.close()
    mixUrls = []
    for url in speechUrls:
        if url not in listFile:
            mixUrls.append(url)
    return mixUrls

def storeMasterUrlsToFile(masterUrls):
    with open('masterUrls.txt', 'w') as f:
        for url in masterUrls:
            f.write(url + '\n')
    f.close()
    return None


speechUrls = getSpeechUrls()
masterUrls = removeDuplicateUrls(speechUrls)
storeMasterUrlsToFile(masterUrls)



