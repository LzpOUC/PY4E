import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

# Retrieve all of the anchor tags
tags = soup('a')
print('Retrieving: ', url.strip())

def retrieves(link):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    print('Retrieving: ', tags[position].get('href', None).strip())
    return tags[position].get('href', None)

for i in range(0, count):
    url = retrieves(url)
