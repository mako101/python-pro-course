from bs4 import BeautifulSoup as bs
import urllib.request as r
from lxml import etree as e

# first we open a URL with urllib
req = r.urlopen('http://www.linuxtoday.com/biglt.rss')

xml = bs(req, 'xml')
# print(xml)


# get just the links from the feed
for item in xml.findAll('link'):
    url = item.text  # extract just the content of tags
    print(20 * '#', '\n', url)


# processing each feed(item) by tags!
items = xml.findAll('item')
for item in items:
    # print(type(item))
    # print(type(item.title))
    print('Feed Title:', item.title.text)
    print('\tDescription:', item.description.text)
    print('\tLink:', item.link.text)
    print('\tDate:', item.pubDate.text)
    print()

