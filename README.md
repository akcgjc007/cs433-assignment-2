# Computer Networks | CN433 | Assignment 2

- truncate -s 10K Test.txt
- ls -l
- cat novels/1080-0.txt > Test.txt
- md5sum novels/1080-0.txt | awk '{print $1}'
- md5sum Test.txt | awk '{print $1}'
- diff `md5sum novels/1080-0.txt | awk '{print $1}'` `md5sum Test.txt | awk '{print $1}'`
- cmp novels/1080-0.txt Test.txt
