import urllib.request, urllib.parse, urllib.error
import ssl
import json

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if(len(url) < 1): url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

sum = 0

js = json.loads(data)
print('Count:', len(js['comments']))
for item in js['comments']:
    sum += int(item['count'])

print('Sum:', sum)
