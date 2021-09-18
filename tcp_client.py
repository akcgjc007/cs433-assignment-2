import socket
from os import getpid
from sys import argv
from time import time
from novels.novel_list import novel_list

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server
BUFFER_SIZE = 1024  # The buffer size to be used

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    start = time()
    s.connect((HOST, PORT))

    # for i in range(len(list_of_books)):
    #     print(i+1, "-", list_of_books[i])
    # print("Enter a book no.:")
    # num = int(input())
    num = int(argv[1])
    if num < 1 or num > 6:
        raise Exception("Incorrect input")

    text = novel_list[num-1]
    res = bytes(text, 'utf-8')
    s.sendall(res)

    all_data = b''
    data = s.recv(BUFFER_SIZE)
    while data:
        all_data += data
        data = s.recv(BUFFER_SIZE)

    # print("Client received:", str(all_data, 'utf-8'))

    text_file = open(text+"_tcp_"+str(getpid())+".txt", "w")
    text_file.write(str(all_data, 'utf-8'))
    text_file.close()

    print("File recieved.")
    end = time()
    print("Total time elapsed:", int((end - start)*1000000))
    print("Throughput:", 10000/(end - start))
