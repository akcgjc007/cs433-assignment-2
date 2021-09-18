# Computer Networks | CN433 | Assignment 2

## Answers

- Check [answers.md](answers.md)

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
