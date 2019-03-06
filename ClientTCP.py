#Shane Harris
from socket import *
serverName = '127.0.0.1'
serverPort = 54788
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
sentence = str.encode(sentence,'utf-8')
#do not need to specify too because the connection is already established
clientSocket.send(sentence)
modifiedMessage = clientSocket.recv(1024).decode("utf-8")
print('From Server:', modifiedMessage)
clientSocket.close()
