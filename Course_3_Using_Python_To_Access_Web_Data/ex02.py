import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter url:")
data = urllib.request.urlopen(url).read()

info = json.loads(data)

comments = info['comments']
x = 0
for item in comments :
    num = int(item['count'])
    x = x + num

print(x)
