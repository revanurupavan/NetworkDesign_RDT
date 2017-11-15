# Pavan Kumar Revanuru
# Network Design
# Code reference: Computer Networking, A Top Down Approach - Page 161

import socket
host = 'localhost'
port = 15000
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ss.bind((host, port))
print " ready"
while 1:
    message, clientAddress = ss.recvfrom(2048)
    modmessage = message.upper()
    ss.sendto(modmessage, clientAddress)
