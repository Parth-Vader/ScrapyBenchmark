# -*- coding: utf-8 -*-
from os.path import join, dirname
from scrapy import Spider
import broad


class RequestsSpider(Spider):
    name = "requests"

    def _requests(self):
        filename = join(dirname(broad.__file__),
                        self.settings.get('SEEDS', ))
        for line in open(filename):
            yield line.strip()

    @classmethod
    def from_crawler(cls, crawler):
        spider = super(RequestsSpider, cls).from_crawler(crawler)
        spider.settings = crawler.settings
        spider.g = spider._requests()
        return spider

    def start_requests(self):
        for url in self.g:
            try:
                yield self.make_requests_from_url(url)
            except:
                self.logger.error('Problem link {}'.format(url))

    def parse(self, response):
        yield {
            'url': response.url
        }
