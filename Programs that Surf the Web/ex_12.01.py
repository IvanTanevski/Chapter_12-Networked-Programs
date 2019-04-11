# Exercise 1: Change the socket program socket1. py to prompt the user for the URL so it can read any web page. 
# You can use split('/') to break the URL into its component parts so you can extract the host name for the 
# socket connect call. Add error checking using try and except to handle the condition where the user enters an
# improperly formatted or non-existent URL.

# Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Locations 3000-3004). Kindle Edition. 

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter URL - ')

try:
    words = url.split('/')                   # Splitting the url and extracting second list item to get
    mysock.connect((words[2], 80))           # the host name (EX- words:['http:', '', 'data.pr4e.org', 'intro-short.txt'])
except:                                      # Actual - http://data.pr4e.org/intro-short.txt
    print('Invalid Url!')
    exit()

cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()   # Creating string command in one string, and encode it
mysock.send(cmd)                                      # Sending the command to mysocket

while True:                                           # Receiving the data in 512 character chunks
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()