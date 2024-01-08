import socket;

s = socket.socket();

HOST= socket.gethostname()
PORT= 8080

s.bind((HOST,PORT))
s.listen(1)

print('Waiting for any incoming connections...')
print(HOST)
conn,addr = s.accept()
print(addr, "Has connected to the server")

filename = input(str('Please enter the filename of the file: '))
file = open(filename, 'rb')
filedata = file.read(1024)
conn.send(filedata)
print('Data has been successfully transmitted ⎘')