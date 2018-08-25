import socket
import pickle
import sys, os

req_code = int(sys.argv[1])


# create server socket using IPv4 and type
def create_socket(type):
    serverSocket = socket.socket(socket.AF_INET, type)
    serverSocket.bind(('', 0))
    return serverSocket


#handshaking step
# recevie the request code and if it is valid, send to UDP socket port
def tcp_init(welcome_socket):
    welcome_socket.listen(1)
    temp = 1
    # listen indefinitely
    while temp:
        connectionSocket, addr = welcome_socket.accept()

        #verify the request code
        received_req_code = pickle.loads(connectionSocket.recv(2048))
        if received_req_code != req_code:
            print('Incorrect Request Code Received')
        else:
            print(received_req_code)
            newSocket = create_socket(socket.SOCK_DGRAM)
            #return port number where server will actually be listening
            connectionSocket.send(pickle.dumps(newSocket.getsockname()[1]))
            temp = 0
        #close the listening socket
        connectionSocket.close()
    return newSocket

# Transaction using UDP
def udpStage(udpSocket):
    message, addr = udpSocket.recvfrom(2048)
    #reverse the message
    modifiedMessage = message.decode()[::-1]
    print(modifiedMessage)
    udpSocket.sendto(modifiedMessage.encode(), addr)
    udpSocket.close()


#main function
# create listening socket
welcome_socket = create_socket(socket.SOCK_STREAM)
print('SERVER_PORT={}'.format(welcome_socket.getsockname()[1]))
while True:
    udpSocket = tcp_init(welcome_socket)
    udpStage(udpSocket)
