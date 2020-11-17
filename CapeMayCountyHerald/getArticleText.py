from selenium import webdriver

# url = ('https://www.capemaycountyherald.com/opinion/columns/article_e80d3e36-4212-11ea-9b60-3f303a9f5eee.html')
# driver = webdriver.Chrome('chromedriver.exe')

def getArticleText(driver, url):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome('../../PycharmProjects/ArticlesDownloadSave/chromedriver.exe', options=options)
    driver.get(url)


    # content = driver.find_elements_by_tag_name("div[itemprop='articleBody']")
    # ret = ""
    # for webelement in content:
    #     ret+=webelement.text
    # driver.close()
    # return ret
