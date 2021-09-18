import socket
from math import ceil
from novels.novel_list import novel_list

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server
BUFFER_SIZE = 1024  # The buffer size to be used

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((HOST, PORT))

print("UDP Server is up.")
print("Listening at:", HOST+":"+str(PORT))
print()

# Listen for incoming datagrams
while(True):
    message, address = UDPServerSocket.recvfrom(BUFFER_SIZE)

    print("Connected to:", address)
    book_name = str(message, "utf-8")
    print("Query for book:", book_name)

    if book_name in novel_list:
        print("Book found, sending now.")
        # Open a file: file
        file = open("./novels/"+book_name+".txt", mode='r')
        # read all lines at once
        all_data = bytes(file.read(), 'utf-8')
        # close the file
        file.close()

        for i in range(ceil(len(all_data)/BUFFER_SIZE)):
            UDPServerSocket.sendto(
                all_data[BUFFER_SIZE*i:BUFFER_SIZE*(i+1)], address)
        UDPServerSocket.sendto(b'END', address)
    else:
        print("Book not found.")
        UDPServerSocket.sendto(bytes("Your book not found", 'utf-8'))

    print("Disconnected from:", address)
    print()
