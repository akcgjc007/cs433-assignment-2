# Computer Networks | CN433 | Assignment 2

- truncate -s 10K Test.txt
- cat novels/'A Modest Proposal.txt' > Test.txt
- md5sum novels/'A Modest Proposal.txt' | awk '{print $1}'
- md5sum Test.txt | awk '{print $1}'
- cmp novels/'A Modest Proposal.txt' Test.txt

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

## Packet monitoring

- For monitoring using `tcpdump`:

  - `sudo tcpdump -vv -x -X -s 1500 -i any 'port 12345'`

- For wireshark, enter this in search bar:

  - `tcp.port eq 12345 || udp.port eq 12345`
