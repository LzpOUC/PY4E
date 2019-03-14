from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignort SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0

tags = soup('span')
for tag in tags:
    attr = tag.attrs['class']
    if attr[0] == 'comments':
        sum += int(tag.contents[0])

print('Sum', sum)
