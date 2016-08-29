from bs4 import BeautifulSoup as bs
import urllib.request as r
from lxml import etree as e

# first we open a URL with urllib
req = r.urlopen('http://www.linuxtoday.com/biglt.rss')

xml = bs(req, 'xml')
# print(xml)

print(type(xml.findAll('item')))

# for item in xml.findAll('link'):
#     url = item.text  # extract just the content of tags
#     print(20 * '#', '\n', url)


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


channel = xml.findAll('channel')
# print(channel_info) # ths returns the whole doc
print(channel.index(1))

# using lxml parser directly:
#
# all_feeds = xml.findAll('item')
#
# for item in all_feeds:
#     # we need to convert the result set into string and then convert it into XML :-/
#     item = str(item)
#     print(item)
#     feed = e.fromstring(item)
#     print(feed)
#     # Now we can pull individual elements out
#     title = feed.find('title')
#     link = feed.find('link')
#     description = feed.find('description')
#     date = feed.find('pubDate')
#
#     print(link.text)

# print('\n', one_item, '\n')
#
# feed = e.fromstring(one_item)
#
#
# print(type(link))
#
#
# print(description.text)
# print(link.text)



# for item in list(xml.findAll('item')):
#     #print(20 * '#', '\n', item)
#     link = xml.findAll('link')
#     #url = link.text
#     description = xml.findAll('description')
#     #desc = description.text
#     print(20 * '#', '\n',description, '\n', link)

