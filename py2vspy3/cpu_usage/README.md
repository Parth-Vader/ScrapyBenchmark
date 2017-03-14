# CPU and Memory usage for Python 2 vs Python 3

I ran `ps aux` alongside `scrapy runspider youtube.py` and recorded the values.


* `python 2.7`

      parth     7127 75.0  0.8 180988 65428 pts/2    S+   15:19   0:00 /usr/bin/python /usr/local/bin/scrapy runspider youtube.py

      parth     7127 75.0  0.8 180988 65428 pts/2    S+   15:19   0:00 /usr/bin/python /usr/local/bin/scrapy runspider youtube.py

      parth     7127 37.5  0.8 180988 65428 pts/2    S+   15:19   0:00 /usr/bin/python /usr/local/bin/scrapy runspider youtube.py

      parth     7127  8.8  0.9 194724 79776 pts/2    S+   15:19   0:01 /usr/bin/python /usr/local/bin/scrapy runspider youtube.py

* `python 3.5.2`

      parth     7326 78.0  0.8 181244 65660 pts/19   S+   15:21   0:00 /usr/bin/python /usr/local/bin/scrapy runspider ../py2vspy3/youtube.py

      parth     7326 39.5  0.8 181376 66280 pts/19   S+   15:21   0:00 /usr/bin/python /usr/local/bin/scrapy runspider ../py2vspy3/youtube.py

      parth     7326 40.0  0.8 182528 67336 pts/19   S+   15:21   0:00 /usr/bin/python /usr/local/bin/scrapy runspider ../py2vspy3/youtube.py

      parth     7326  9.6  0.9 194692 79776 pts/19   S+   15:21   0:01 /usr/bin/python /usr/local/bin/scrapy runspider ../py2vspy3/youtube.py


As we can see from the stats from `ps aux` for `scrapy runspider youtube.py`,

* `python 3.5.2` uses a little more CPU time.

* The memory usage is same for both.

* The virtual memory usage of entire process (in KiB) is a little higher for `python 2.7`

* The resident set size is exactly same at the last for both.
