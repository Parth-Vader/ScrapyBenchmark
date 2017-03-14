# Python 2 vs Python 3 performance

When `scrapy bench` was run with `python2.7` and `python3`, there was some difference in the speed.

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

