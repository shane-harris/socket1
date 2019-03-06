#Shane Harris
from socket import *
#use a unique port because they can be reserved
HOST = ''
serverPort = 54787
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((HOST, serverPort))
print('The server is ready to recieve')
while 1:
    message, clientAddress = serverSocket.recvfrom(20448)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
#serverSocket.close()
