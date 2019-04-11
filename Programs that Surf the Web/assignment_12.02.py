# Following Links in Python
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat 
# the process a number of times and report the last name you find.


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Jason.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = 7
position = 18

for i in range(count):                              # Repeating the loop in range of count(7) times,
    html = urllib.request.urlopen(url).read()       # and finding the position 18 (the 18th href link) each time
    soup = BeautifulSoup(html, 'html.parser')       # another loop iterates inside (follows the 18th link).
    tags = soup('a')                                # In the last (7th) iteration (7 times following the 18th position) the
    num = 0                                         # contents of the 'href' tag i.e. the name is printed by the program.
    for tag in tags:                                
        num += 1
        if num == position:
            url = tag.get('href')
            if i == count - 1:
                print(tag.contents[0])
