from selenium import webdriver

def OpenPage(url):
    driver = webdriver.Chrome('chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.headless = True
    driver.get(url)
