# Scraping Numbers from HTML using BeautifulSoup. In this assignment you will write a Python program similar to 
# http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, 
# and parse the data, extracting numbers and compute the sum of the numbers in the file.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_210706.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags, count them, and sum their values
count = 0
total = 0
tags = soup('span')
for tag in tags:
    total += int(tag.contents[0])
    count += 1
print('Count =', count)
print('Total =', total)