#  Pavan kumar Revanuru
#  Network design
#  Code Reference: Computer Networking, A Top Down approach - Page 159
  


import socket
host = 'localhost'
port = 15000
cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file = open('test.txt', 'r')
message = file.read(2048)
cs.sendto(message, (host, port))
modmessage, serverAddress = cs.recvfrom(2048)
print modmessage
f = open('new.txt', 'w')
f.write(modmessage)
f.close()
cs.close()
