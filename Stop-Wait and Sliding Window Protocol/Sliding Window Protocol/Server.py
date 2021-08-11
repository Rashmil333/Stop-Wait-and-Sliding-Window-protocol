import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

serversocket.bind((host, port))


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            window_size=int(input("Enter the window size"))
            arra=list(map(int,input("Enter the Frames of the data").split()))
            counter=len(arra)-1
            start=0
            i=0
            while(i<=counter):
                for k in range(start,start+window_size):
                    if(k<=counter):
                        clientsocket.send(str(arra[k]).encode())
                        print("Acknowledge receiver for data--->", clientsocket.recv(1024).decode())
                        start+=1
                        i+=1
                    else:
                        break
                print("Window is Sliding")






serversocket.listen(5)
print('Sender ready and is listening')
while (True):
    # to accept all incoming connections
    clientsocket, address = serversocket.accept()
    print("Receiver " + str(address) + " connected")
    # create a different thread for every
    # incoming connection
    client(clientsocket, address)