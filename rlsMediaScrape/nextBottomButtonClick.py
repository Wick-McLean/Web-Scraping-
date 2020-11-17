from selenium.common.exceptions import NoSuchElementException
from getPageUrls import getUrls
from selenium import webdriver

driver = webdriver.Chrome()

def clickNext(driver):
    while True:
        try:
            getUrls()
            elem = driver.find_element_by_link_text("Next")
            elem.click()

        except NoSuchElementException:
            print("Last Page")
            return True
