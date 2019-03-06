#Shane Harris
from socket import *
HOST = ''
serverPort = 54788
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST,serverPort))
serverSocket.listen(1)
print('The server is Ready to recieve')
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
#serverSocket.close()

