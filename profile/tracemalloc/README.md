# Using tracemalloc for profiling

Do the following : 

* cd youtube/youtube/spiders
* python ../trace.py

### This program calls the spider using `subprocess` module in the file itself, and displays the 10 lines allocating the most memory with a pretty output, ignoring `frozen importlib._bootstrap` and `unknown` files.

The output for the `youtube2.py` file is :

		Top 10 lines
		#1: python3.4/abc.py:133: 12.1 KiB
		#2: collections/__init__.py:364: 10.5 KiB
		#3: python3.4/_weakrefset.py:37: 7.0 KiB
		#4: python3.4/subprocess.py:742: 5.8 KiB
		#5: python3.4/_weakrefset.py:38: 5.0 KiB
		#6: python3.4/_weakrefset.py:48: 4.2 KiB
		#7: python3.4/threading.py:733: 3.3 KiB
		#8: python3.4/threading.py:729: 3.1 KiB
		#9: python3.4/threading.py:364: 2.5 KiB
		#10: python3.4/threading.py:88: 2.4 KiB
		312 other: 98.1 KiB
		Total allocated size: 154.1 KiB

