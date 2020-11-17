# from selenium import webdriver

def capeHeraldGetPageUrls(driver, url):
    driver.get(url)
    content = driver.find_elements_by_tag_name('a.tnt-asset-link')
    urls = []
    for link in content:
        urls.append(link.get_attribute('href'))
    driver.close()
    return urls

