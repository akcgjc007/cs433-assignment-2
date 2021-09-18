import socket
from os import getpid
from sys import argv
from time import time, sleep
from novels.novel_list import novel_list

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server
BUFFER_SIZE = 1024  # The buffer size to be used

start = time()


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

num = int(argv[1])
if num < 1 or num > 6:
    raise Exception("Incorrect input")

text = novel_list[num-1]
res = bytes(text, 'utf-8')

# Send to server using created UDP socket
UDPClientSocket.sendto(res, (HOST, PORT))

all_data = b''
data = UDPClientSocket.recvfrom(BUFFER_SIZE)
while data[0] != b'END':
    sleep(0.001)
    all_data += data[0]
    print(len(data[0]), len(data[1]))
    data = UDPClientSocket.recvfrom(BUFFER_SIZE)

text_file = open(text+"_udp_"+str(getpid())+".txt", "w")
text_file.write(str(all_data, 'utf-8'))
text_file.close()

print("File recieved.")
end = time()
print("Total time elapsed:", int((end - start)*1000000))
