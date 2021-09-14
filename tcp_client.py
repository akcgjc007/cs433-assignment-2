import socket
from os import getpid
from sys import argv

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    list_of_books = ['A Modest Proposal',
                     'How to Get Married, Although a Woman or, The Art of Pleasing Men',
                     'Old Granny Fox',
                     'Roses: or a Monograph on The Genus Rosa',
                     'The Atom and the Ocean']

    # for i in range(len(list_of_books)):
    #     print(i+1, "-", list_of_books[i])
    # print("Enter a book no.:")
    # num = int(input())
    num = int(argv[1])
    if num < 1 or num > 5:
        raise Exception("Incorrect input")

    text = list_of_books[num-1]
    res = bytes(text, 'utf-8')
    s.sendall(res)

    all_data = b''
    data = s.recv(1024)
    while data:
        all_data += data
        data = s.recv(1024)

    # print("Client received:", str(all_data, 'utf-8'))

    text_file = open(text+"_tcp_"+str(getpid())+".txt", "w")
    text_file.write(str(all_data, 'utf-8'))
    text_file.close()

    print("File recieved.")
