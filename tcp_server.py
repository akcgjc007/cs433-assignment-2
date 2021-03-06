import socket
from novels.novel_list import novel_list

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server
BUFFER_SIZE = 1024  # The buffer size to be used

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # https://stackoverflow.com/a/4466035/12552972
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((HOST, PORT))
        print("TCP Server is up.")
        print("Listening at:", HOST+":"+str(PORT))
        print()
        s.listen()
        conn, addr = s.accept()

        print("Connected to:", addr)
        data = conn.recv(BUFFER_SIZE)

        book_name = str(data, "utf-8")
        print("Query for book:", book_name)

        if book_name in novel_list:
            print("Book found, sending now.")
            # Open a file: file
            file = open("./novels/"+book_name+".txt", mode='r')
            # read all lines at once
            all_of_it = file.read()
            # close the file
            file.close()
            conn.sendall(bytes(all_of_it, 'utf-8'))
        else:
            print("Book not found.")
            conn.sendall(bytes("Your book not found", 'utf-8'))

        print("Disconnected from:", addr)
        print()
        conn.close()
