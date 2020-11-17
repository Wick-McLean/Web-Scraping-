from getAhref import getAhref
from LinkRipper import linkRipper

url = ('https://nypost.com/')
urlData = getAhref(url)
finals = linkRipper(urlData)
print(finals)