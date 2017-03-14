# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from scrapy.spiders import BaseSpider
#from scrapy import log
from scrapy.cmdline import execute
from scrapy.utils.markup import remove_tags
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.extensions.logstats import LogStats


import time

#define spider
class BenchSpider(scrapy.Spider):
	
	name = 'bench'
	#allowed_domains = ["https://www.youtube.com"]
	start_urls = ['https://www.github.com']
	#time.sleep(10)
	link_extractor = LinkExtractor()
	custom_settings = {
        'DEPTH_LIMIT': '2',
        'MEMUSAGE_CHECK_INTERVAL_SECONDS' : '2',
	}
#selectors
	def parse(self, response):
		count = 0
		for link in self.link_extractor.extract_links(response):
			#count = count+1
			#print "count is "
			#print count 
			#if count <=100 :
				yield scrapy.Request(link.url, callback=self.parse)
			#else :
			#	break	
