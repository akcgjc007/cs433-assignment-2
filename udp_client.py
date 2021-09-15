import socket
from os import getpid
from sys import argv
from time import time

msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

start = time()


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

list_of_books = ['A Modest Proposal',
                 'How to Get Married, Although a Woman or, The Art of Pleasing Men',
                 'Old Granny Fox',
                 'Roses: or a Monograph on The Genus Rosa',
                 'The Atom and the Ocean']
num = int(argv[1])
if num < 1 or num > 5:
    raise Exception("Incorrect input")

text = list_of_books[num-1]
res = bytes(text, 'utf-8')

# Send to server using created UDP socket
UDPClientSocket.sendto(res, serverAddressPort)

all_data = b''
data = UDPClientSocket.recvfrom(bufferSize)
while data[0] != b'END':
    all_data += data[0]
    data = UDPClientSocket.recvfrom(bufferSize)

text_file = open(text+"_udp_"+str(getpid())+".txt", "w")
text_file.write(str(all_data, 'utf-8'))
text_file.close()

print("File recieved.")
end = time()
print("Total time elapsed:", end - start)
