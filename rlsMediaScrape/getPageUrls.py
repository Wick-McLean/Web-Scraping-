from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.fmprc.gov.cn/mfa_eng/wjdt_665385/zyjh_665391/')

def getUrls(driver):
    elem = driver.find_elements_by_tag_name('a')
    ret = ''
    for href in elem:
        ret += href.get_attribute('href')
    return ret



    # speechUrls = []
    # for urls in elem:
    #     driver.find_element_by_tag_name('href')
    #     speechUrls.append(urls)


#Run this only if user manually says to run it
if __name__ == "__main__":
    getUrls(driver)


