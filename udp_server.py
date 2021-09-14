import socket
from os import listdir
from math import ceil

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP Server is up.")
print("Listening at:", localIP+":"+str(localPort))
print()

# Listen for incoming datagrams
while(True):
    message, address = UDPServerSocket.recvfrom(bufferSize)

    print("Connected to:", address)
    book_name = str(message, "utf-8")
    print("Query for book:", book_name)

    all_books = [i[:-4] for i in listdir("./novels")]
    if book_name in all_books:
        print("Book found, sending now.")
        # Open a file: file
        file = open("./novels/"+book_name+".txt", mode='r')
        # read all lines at once
        all_data = bytes(file.read(), 'utf-8')
        # close the file
        file.close()

        for i in range(ceil(len(all_data)/bufferSize)):
            UDPServerSocket.sendto(
                all_data[bufferSize*i:bufferSize*(i+1)], address)
        UDPServerSocket.sendto(b'END', address)
    else:
        print("Book not found.")
        UDPServerSocket.sendto(bytes("Your book not found", 'utf-8'))

    print("Disconnected from:", address)
    print()
