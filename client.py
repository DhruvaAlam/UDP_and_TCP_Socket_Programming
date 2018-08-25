from socket import *
import sys, os
import pickle

#Extract command line arguments and validate
if len(sys.argv) != 5:
    print('Not enough command line arguments. Exiting')
    os._exit(1)

server_address = sys.argv[1]
try:
    n_port = int(sys.argv[2])
except:
    print('Port command line argument is not valid')
    os._exit(1)
req_code = int(sys.argv[3])
msg = sys.argv[4]


def handShake():
    #create client socket for tcp connection
    clientSocket = socket(AF_INET, SOCK_STREAM)

    #innitiate TCP connection between the client and server
    clientSocket.connect(((server_address, n_port)))
    clientSocket.send(pickle.dumps(req_code))
    try:
        actual_port = pickle.loads(clientSocket.recv(2048))
    except:
        print("req_code does not match")
        clientSocket.close()
        quit()
    #close tcp connection
    clientSocket.close()
    return actual_port

def reverseMessageUDP(r_port):
    #create UDP socket
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    #send message to r_port and server_address of the server
    udpSocket.sendto(msg.encode(), (server_address, r_port))
    modifiedMessage, addr = udpSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    udpSocket.close()

reverseMessageUDP(handShake())
