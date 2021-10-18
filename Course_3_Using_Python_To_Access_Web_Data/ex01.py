import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter URL:")
xml = urllib.request.urlopen(url).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
t = 0
for count in counts :
    c = (count.text)
    t = t + int(c)
print(t)
