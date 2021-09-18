## 1

Installed.

## 2

5 novels selected:

- 'A Modest Proposal.txt'
- 'How to Get Married, Although a Woman or, The Art of Pleasing Men.txt'
- 'Old Granny Fox.txt'
- 'Roses: or a Monograph on The Genus Rosa.txt'
- 'The Atom and the Ocean.txt'

### 2 b)

- truncate -s 10K Test.txt
- cat novels/book1.txt > Test.txt
- md5sum novels/book1.txt | awk '{print $1}'
- md5sum Test.txt | awk '{print $1}'
- cmp novels/book1.txt Test.txt

## 3

For running, you can use:

- python3 tcp_server.py
- `python3 tcp_client.py 3` ( the argument represents the book needs to be downloaded. 1-5 represents book, while 6 represents a test file. )
- similar commands for udp server

## 3.1

---

|         | Largest file-TCP(in us) | Throughput  | Largest file-UDP(in us) | Throughput  | Test-file-TCP(in us) | Throughput  | Test-file-UDP(in us) | Throughput  |
| ------- | ----------------------- | ----------- | ----------------------- | ----------- | -------------------- | ----------- | -------------------- | ----------- |
| 1       | 5808                    | 33.47055785 | 5018                    | 38.73993623 | 423                  | 24.20803783 | 587                  | 17.44463373 |
| 2       | 6177                    | 31.47110248 | 7169                    | 27.11633422 | 432                  | 23.7037037  | 448                  | 22.85714286 |
| 3       | 5576                    | 34.86316356 | 4952                    | 39.2562601  | 526                  | 19.46768061 | 535                  | 19.14018692 |
| 4       | 6217                    | 31.2686183  | 6856                    | 28.35428821 | 449                  | 22.80623608 | 547                  | 18.7202925  |
| 5       | 5927                    | 32.79854901 | 6144                    | 31.64013672 | 386                  | 26.52849741 | 480                  | 21.33333333 |
| 6       | 5693                    | 34.14667135 | 5664                    | 34.32150424 | 696                  | 14.71264368 | 428                  | 23.92523364 |
| 7       | 6137                    | 31.67622617 | 6056                    | 32.09990092 | 486                  | 21.06995885 | 586                  | 17.47440273 |
| 8       | 5851                    | 33.224577   | 5423                    | 35.84676378 | 377                  | 27.16180371 | 450                  | 22.75555556 |
| 9       | 5662                    | 34.33362769 | 5774                    | 33.66764808 | 453                  | 22.60485651 | 472                  | 21.69491525 |
| 10      | 6684                    | 29.08393178 | 5846                    | 33.2529935  | 491                  | 20.85539715 | 459                  | 22.30936819 |
| Average | 5973.2                  | 32.54486707 | 5890.2                  | 33.00346338 | 471.9                | 21.69951261 | 499.2                | 20.51282051 |

---

## 3.2

Already mentioned in above answer.

## 3.3

Sometimes, the files are showing differences.

The diff command is giving very big output.

```
pam@g3:~/Desktop/CS-433/ass2$ wc novels/book1_tcp_53232.txt
2800  25852 142385 novels/book1.txt
2800  25852 139585 book1_tcp_53232.txt
```

## Exp A

|            | Packets on Wireshark | Actual file size | Received file size | diff command      |
| ---------- | -------------------- | ---------------- | ------------------ | ----------------- |
| tcp - 2048 | 11                   | 39819            | 39094              | large output seen |
| udp - 2048 | 41                   | 39819            | 39094              | large output seen |
|            |                      |                  |                    |                   |
| tcp-512    | 11                   | 39819            | 39094              | large output seen |
| udp-512    | 41                   | 39819            | 19638              | large output seen |
|            |                      |                  |                    |                   |
| tcp-q3     | 11                   | 39819            | 39094              | large output seen |
| udp-q3     | 79                   | 39819            | 39094              | large output seen |
|            |                      |                  |                    |                   |
| tcp-10ms   | 13                   | 39819            | 39094              | large output seen |
| udp-10ms   | 51                   | 39819            | 39094              | large output seen |

## Exp 5

Referencing: https://stackoverflow.com/questions/6437383/can-tcp-and-udp-sockets-use-the-same-port

As discussed in the above port, each request is made of a quintuple consists of source IP, dest. IP, source port, dest. port and protocol(TCP or UDP). Hence, both ports can be used at the same time.
