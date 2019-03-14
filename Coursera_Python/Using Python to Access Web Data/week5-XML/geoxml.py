import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

output = 0

url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')
# print(data)
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count: ', len(counts))
for count in counts:
    output += int(count.text)

print('Sum: ', output)
