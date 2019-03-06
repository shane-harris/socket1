#Shane Harris
from socket import *
serverName = '127.9.5.1'
#this port number must be the same as the one originally inputed in the top part
serverPort = 54787
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
#must know the send to
message = message.encode('utf-8')
clientSocket.sendto(message, (serverName, serverPort))
#recieve from because we want to know who we got the message from
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
modifiedMessage = modifiedMessage.decode('utf-8')
print(modifiedMessage)
clientSocket.close()
#the socket must close otherwise the line will stay open
