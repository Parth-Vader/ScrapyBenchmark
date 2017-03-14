# scrapy bench

File `benchnew.py` is meant to be in addition with the existing `scrapy bench`.

This file is a simple spider which just extracts the links from the given link.

In this case, I have used base_url = `www.github.com`. The following are the custom settings:

	`custom_settings = {
		    'DEPTH_LIMIT': '2',
		    'MEMUSAGE_CHECK_INTERVAL_SECONDS' : '2',
	}`
	

After doing `scrapy runspider benchnew.py`, the logstats are as follows :


		[scrapy.extensions.logstats] INFO: Crawled 1294 pages (at 146 pages/min), scraped 0 items (at 0 items/min)
		[scrapy.extensions.logstats] INFO: Crawled 1298 pages (at 2 pages/min), scraped 0 items (at 0 items/min)


Important stats : 
		'downloader/request_bytes': 1740150,
		'downloader/request_count': 2764,
		'downloader/request_method_count/GET': 2764,
		'downloader/response_bytes': 44107613,
		'downloader/response_count': 2740,
		'downloader/response_status_count/200': 1307,
		'downloader/response_status_count/301': 1411,
		'downloader/response_status_count/302': 20,
		'downloader/response_status_count/404': 2,
		'dupefilter/filtered': 732,

This is in contrast with `scrapy bench` : 
		'downloader/request_bytes': 239399,
		'downloader/request_count': 774,
		'downloader/request_method_count/GET': 774,
		'downloader/response_bytes': 1147582,
		'downloader/response_count': 774,
		'downloader/response_status_count/200': 774,
		'dupefilter/filtered': 1092,
		
The `scrapy runspider benchnew.py` ran for around 10 minutes, while `scrapy bench` ran for around 10 seconds.

Hence, the importance of real-life webpages for benchmarking can be seen.

