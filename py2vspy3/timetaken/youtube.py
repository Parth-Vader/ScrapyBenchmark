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

import time

#define spider
class YoutubeSpider(scrapy.Spider):
	name = 'youtube_spider'
	#allowed_domains = ["https://www.youtube.com"]
	start_urls = ['https://www.youtube.com/watch?v=2gnDgs-xVAo']
	#time.sleep(10)

	custom_settings = {
        'DEPTH_LIMIT': '100',
	}
#selectors
	#@profile
	def parse(self, response):
		SET_SELECTOR = '#page-container'
		#NEW_SELECTOR = '#watch-header'
		for youtube in response.css(SET_SELECTOR,):


			TITLE_SELECTOR = 'meta ::attr(content)'
			LINK_SELECTOR = 'link ::attr(href)'
			VIEWCOUNT_SELECTOR = '//*[@id="watch7-views-info"]/div[1]/text()'
			DATEPUB_SELECTOR = '//*[@id="watch7-content"]/meta[14]/@content'
			GENRE_SELECTOR = '//*[@id="watch7-content"]/meta[15]/@content'
			NAME_SELECTOR = '//*[@id="watch7-user-header"]/div/a/text()'
			SUBS_SELECTOR = '//*[@id="watch7-subscription-container"]/span/span[1]/text()'
			LIKES_SELECTOR = '//*[@id="watch8-sentiment-actions"]/span/span[1]/button/span/text()'
			DISLIKES_SELECTOR = '//*[@id="watch8-sentiment-actions"]/span/span[3]/button/span/text()'
			#COMMENT_SELECTOR = '//*[@id="comment-section-renderer"]/text()'
			yield {
				'Video Title': youtube.css(TITLE_SELECTOR).extract_first(),
				'Video Link': youtube.css(LINK_SELECTOR).extract_first(),
				'Number of Views': youtube.xpath(VIEWCOUNT_SELECTOR).extract()[0].replace("views", ""),
				'Date Uploaded': youtube.xpath(DATEPUB_SELECTOR).extract_first(),
				'Video Category': youtube.xpath(GENRE_SELECTOR).extract_first(),
				'User Name': youtube.xpath(NAME_SELECTOR).extract_first(),
				'Number of Subscribers': youtube.xpath(SUBS_SELECTOR).extract_first(),
				'Likes Received': youtube.xpath(LIKES_SELECTOR).extract_first(),
				'Dislikes Received': youtube.xpath(DISLIKES_SELECTOR).extract_first(),
				#'Number of Comments': youtube.xpath(COMMENT_SELECTOR).extract_first(),
			}
	#get video links in webpage		
			RELATED_SELECTOR = '#watch-related a ::attr(href)'
			next_article = response.css(RELATED_SELECTOR).extract_first()
			if next_article:
				yield scrapy.Request(
					response.urljoin(next_article),
					callback=self.parse, #dont_filter=True 
					)