# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document 
# and display the count of the paragraphs as the output of your program. Do not display the paragraph text, 
# only count them. Test your program on several small web pages as well as some larger web pages.

# Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Locations 3009-3012). Kindle Edition. 


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all paragraph tags and count them
tags = soup('p')
count = 0
for tag in tags:
    count += 1

print(count)