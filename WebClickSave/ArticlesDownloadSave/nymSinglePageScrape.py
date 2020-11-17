from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get("http://nymag.com/intelligencer/2019/04/andrew-sullivan-impeach-trump-now.html")
driver.implicitly_wait(6)


elem = driver.find_element_by_xpath("/html/body/section[6]/section[1]/article/section/div[3]/a")
elem.send_keys(Keys.RETURN)

#New url after pressing return:
currenturl=driver.current_url


#switch to new frame
#
# driver.switch_to.default_content()
driver.implicitly_wait(3)

driver.switch_to.frame("//iframe[@name='_0.9787120723908653_iframe']")

# for i in len(element):
#     print(element.text[i])
#     print(element.tag_name[i])
#     print(element.parent[i])
#     print(element.location[i])
#     print(element.size[i])


driver.implicitly_wait(3)
MoreComments=[]
MoreComments = driver.find_element_by_xpath("//iframe[@name='_0.9787120723908653_iframe']")
print(len(MoreComments))
print(MoreComments)


# MoreComments.send_keys(Keys.RETURN)





driver.quit()