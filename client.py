import socket

s = socket.socket()

HOST=input(str("Please enter the host of the sender: "))
PORT= 8080

s.connect((HOST,PORT));

print('Connected ✅')

filename = input(str("Please enter a filename for the incoming file: "))
file = open(filename, 'wb')
filedata = s.recv(1024)
file.write= (filedata)

file.close()
print('File has been recieved successfully 🥇')