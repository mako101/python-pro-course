# https://docs.python.org/3/library/urllib.html

# urllib.request for opening and reading URLs
# urllib.error containing the exceptions raised by urllib.request
# urllib.parse for parsing URLs
# urllib.robotparser for parsing robots.txt files


# https://docs.python.org/3.1/howto/urllib2.html

from urllib import request as r
import urllib.parse as p
import urllib.error as e


# Basic function to construct and send URL request
# works the same for all URL types:
def print_page(url, **kwargs):
    request = r.Request(url, **kwargs)
    response = r.urlopen(request)
    print(response.read())


## Simple examples of FTP and HTTP requests
# print_page('http://www.bbc.com')
# print_page('ftp://ftp.apotheka.ee/lib/')


# More fancy examples using encoding (from dictionary) and passing headers
url = 'https://www.google.com/search?'
values = {'q': 'python tutorials'}
data = p.urlencode(values, encoding='utf-8')
url = 'https://www.google.com/search?' + data
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686)'}

# print_page(url, data=data, headers=headers) # passing "data" argument turns it into POST, so need to avoid it here
#print_page(url, headers=headers)

# urllib.parse can also parse a given URL into components, with options!
# https://docs.python.org/3.0/library/urllib.parse.html

parsed = p.urlparse('https://en.wikipedia.org/wiki/Wikipedia#/media/File:Wikipedia_editing_interface.png')
#split = p.urlsplit('https://en.wikipedia.org/wiki/Wikipedia#/media/File:Wikipedia_editing_interface.png')

print(parsed)

# We can call the parsed tuple elements!
print('The server is:', parsed.netloc)

# A bit of error handling
print('\nError Handling\n')

print('Invalid URL Example -> Clean message')
try:
    print_page('http://www.pretend_server.org')
except e.URLError as url_error:
    print(str(url_error.reason).split('] ')[1])

print('\nBad HTTP Code Example')
try:
    print_page('https://upload.wikimedia.org/svsfsbf')
except e.HTTPError as http_error:
    print(http_error)

print('\nGeneric Exception Examples - also work!!')
try:
    print_page('https://upload.wikimedia.org/svsfsbf')
except Exception as error:
    print(error)

try:
    print_page('http://www.pretend_server.org')
except Exception as error:
    print(error)
