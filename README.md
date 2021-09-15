# Computer Networks | CN433 | Assignment 2

- truncate -s 10K Test.txt
- ls -l
- cat novels/1080-0.txt > Test.txt
- md5sum novels/1080-0.txt | awk '{print $1}'
- md5sum Test.txt | awk '{print $1}'
- diff `md5sum novels/1080-0.txt | awk '{print $1}'` `md5sum Test.txt | awk '{print $1}'`
- cmp novels/1080-0.txt Test.txt


## TCP Server-Client Communication
- Server listens on a port
- Client accepts a book name from user
- Client sends the book name to the server
- Server recieves the book name from the client
- Server searches the book name in its database
- Server throws error if book not found
- Server sends the book file if book is found
- Server closes the connection
- Client receives the error or the file
- Client shows the output to the user

## Helpful commands
- python3 tcp_server.py
- python3 tcp_client.py
- python3 udp_server.py
- python3 udp_client.py

- Forcefully killing the server: `fuser -k -n tcp 12345`