import json
import requests

r = requests.get("http://nymag.com/_components/nymag-latest-feed/instances/index@published")
formattedlist = r.json()
xyz = formattedlist["manualArticleUrls"]

with open('datas.txt', 'a') as outfile:
    for element in xyz:
        outfile.write(element + "\n" )
outfile.close()