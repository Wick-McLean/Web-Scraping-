from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
url = ('https://www.fmprc.gov.cn/mfa_eng/wjdt_665385/zyjh_665391/')

def getUrls(driver, url):
    driver.get(url)
    elem = driver.find_elements_by_tag_name('a')
    driver.close()
    return elem
    # urls = []
    # for href in elem:
    #     urls.append(href.get_attribute('href'))
    # return urls

def getPastUrls():
    f = open('urlMasterList.txt', 'r')
    var1 = f.readlines()
    f.close()
    return list(map(lambda x: x.replace('\n', ''), var1))

def addUrls(urls):
    f = open('urlMasterList.txt', 'a')
    for url in urls:
        f.write(url) + '\n'
    pass


if __name__ == '__main__':
    print(getUrls(driver, url))


