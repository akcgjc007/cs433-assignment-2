CC := python3

check:
	sudo tcpdump -vv -x -X -s 1500 -i any 'port 12345'

t_s:
	$(CC) tcp_server.py

t_c:
	$(CC) tcp_client.py 1

u_s:
	$(CC) udp_server.py

u_c:
	$(CC) udp_client.py 1
	
clean:
	rm -rf *.txt
