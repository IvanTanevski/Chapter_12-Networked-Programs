# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying 
# any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number
# of characters and display the count of the number of characters at the end of the document.

# Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Locations 3005-3006). Kindle Edition. 


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

count = 0
while True:                                           # Receiving the data in 500 character chunks
    data = mysock.recv(500)                           # If there is data to receive up to 3000 characters, the program
    if len(data) > 1 and count < 3000:                # receives print it
        print(data.decode(),end='')
        count += len(data)
    elif len(data) > 1 and count >= 3000:             # The program only counts the data from 3000 characters above, 
        count += len(data)                            # without printing it
    else:
        break

print()
print('Overall count =', count)
mysock.close()