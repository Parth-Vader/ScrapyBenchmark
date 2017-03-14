# Python 2 vs Python 3 performance

### When `scrapy bench` was run with `python2.7` and `python3`, there was some difference in the speed.

* Stats for `python 2.7`

		2017-03-14 14:01:44 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:45 [scrapy.extensions.logstats] INFO: Crawled 85 pages (at 5100 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:46 [scrapy.extensions.logstats] INFO: Crawled 165 pages (at 4800 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:47 [scrapy.extensions.logstats] INFO: Crawled 237 pages (at 4320 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:48 [scrapy.extensions.logstats] INFO: Crawled 321 pages (at 5040 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:49 [scrapy.extensions.logstats] INFO: Crawled 400 pages (at 4740 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:50 [scrapy.extensions.logstats] INFO: Crawled 473 pages (at 4380 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:51 [scrapy.extensions.logstats] INFO: Crawled 546 pages (at 4380 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:52 [scrapy.extensions.logstats] INFO: Crawled 619 pages (at 4380 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:53 [scrapy.extensions.logstats] INFO: Crawled 699 pages (at 4800 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:01:54 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
		2017-03-14 14:01:54 [scrapy.extensions.logstats] INFO: Crawled 765 pages (at 3960 pages/min), scraped 0 items (at 0 items/min)

* Stats for `python 3.5.2`

		2017-03-14 14:25:16 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:17 [scrapy.extensions.logstats] INFO: Crawled 85 pages (at 5100 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:18 [scrapy.extensions.logstats] INFO: Crawled 166 pages (at 4860 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:19 [scrapy.extensions.logstats] INFO: Crawled 254 pages (at 5280 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:20 [scrapy.extensions.logstats] INFO: Crawled 342 pages (at 5280 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:21 [scrapy.extensions.logstats] INFO: Crawled 408 pages (at 3960 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:22 [scrapy.extensions.logstats] INFO: Crawled 488 pages (at 4800 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:23 [scrapy.extensions.logstats] INFO: Crawled 568 pages (at 4800 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:24 [scrapy.extensions.logstats] INFO: Crawled 633 pages (at 3900 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:25 [scrapy.extensions.logstats] INFO: Crawled 698 pages (at 3900 pages/min), scraped 0 items (at 0 items/min)
		2017-03-14 14:25:26 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
		2017-03-14 14:25:26 [scrapy.extensions.logstats] INFO: Crawled 763 pages (at 3900 pages/min), scraped 0 items (at 0 items/min)


### Furthermore, when a simple spider `youtube.py` is run with `python2` and `python3`, there are time differences.


* `python 2.7` : 

		'downloader/request_bytes': 3652,
		'downloader/request_count': 10,
		'downloader/request_method_count/GET': 10,
		'downloader/response_bytes': 478731,
		'downloader/response_count': 10,
		'downloader/response_status_count/200': 10,
		'dupefilter/filtered': 1,
		'finish_reason': 'finished',
		'finish_time': datetime.datetime(2017, 3, 14, 9, 9, 46, 734378),
		'item_scraped_count': 10,
		'log_count/DEBUG': 22,
		'log_count/INFO': 7,
		'request_depth_max': 10,
		'response_received_count': 10,
		'scheduler/dequeued': 10,
		'scheduler/dequeued/memory': 10,
		'scheduler/enqueued': 10,
		'scheduler/enqueued/memory': 10,
		'start_time': datetime.datetime(2017, 3, 14, 9, 9, 37, 314201)}
		
		
* `python 3.5.2` : 

		'downloader/request_bytes': 3652,
		'downloader/request_count': 10,
		'downloader/request_method_count/GET': 10,
		'downloader/response_bytes': 470069,
		'downloader/response_count': 10,
		'downloader/response_status_count/200': 10,
		'dupefilter/filtered': 1,
		'finish_reason': 'finished',
		'finish_time': datetime.datetime(2017, 3, 14, 9, 9, 31, 486471),
		'item_scraped_count': 10,
		'log_count/DEBUG': 22,
		'log_count/INFO': 7,
		'request_depth_max': 10,
		'response_received_count': 10,
		'scheduler/dequeued': 10,
		'scheduler/dequeued/memory': 10,
		'scheduler/enqueued': 10,
		'scheduler/enqueued/memory': 10,
		'start_time': datetime.datetime(2017, 3, 14, 9, 9, 18, 808820)}
		
The values for `'finish_time' - 'start-time'` are as follows :-

* `python 2.7` : 9.420177 sec
* `python 3.5.2` : 12.677651 sec

Hence, python3 is a little slower than python2 for the spider.

	
