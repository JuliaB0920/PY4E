import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#import ssl

 #Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
numlist = []
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('span', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    nums = numlist.append(int(tag.contents[0]))
print(sum(numlist))
