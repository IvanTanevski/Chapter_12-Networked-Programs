# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. 
# Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

# Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Locations 3007-3009). Kindle Edition. 

import urllib.request

url = input('Enter URL - ')
try:
    html = urllib.request.urlopen(url).read().decode()      # Requesting to open the URL from input, read and decode it
except:
    print('Invalid URL!')
    exit()

html3K = html[0:3000]                                       
print(html3K)                                               # Displaying up to 3000 characters of the read HTML document
count = 0
for x in html:                  
    count += 1                                              # Counting all the characters in the HTML document

print('Displayed up to 3000 characters. Overall count = ', count)