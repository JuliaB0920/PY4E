import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#import ssl

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = (soup('a'))
#print(tags.contents[0])
#nurl = (tags.get('href', None))
#print(nurl)



x = 7
while x > 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = (soup('a'))
    tag2 = tags[17]
    print(tag2.contents)
    url = (tag2.get('href', None))
    x = x - 1

#print('Done')
