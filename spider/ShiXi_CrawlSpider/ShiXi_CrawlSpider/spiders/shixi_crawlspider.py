# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ShiXi_CrawlSpider.items import ShixiCrawlspiderItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class ShixiCrawlspiderSpider(CrawlSpider):
    name = 'shixi_crawlspider'
    allowed_domains = ['shixiseng.com']
    start_urls = ['http://shixiseng.com/']
    rules = (
        Rule(LinkExtractor(allow=r'&p=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        post = response.xpath("//ul/li/div/div[1]/a/text()").extract()
        urls = response.xpath("//ul/li/div/div[1]/a/@href").extract()
        place = response.xpath("//ul/li/div[2]/div[1]/text()").extract()
        money = response.xpath("//ul/li/div[2]/div[2]").extract()
        time = response.xpath("//ul/li/div[2]/div[2]/span[2]").extract()
        for i in range(0, len(post)):
            item = ShixiCrawlspiderItem()
            item['post'] = post[i]
            item['urls'] = urls[i]
            item['place'] = place[i]
            item['money'] = money[i]
            item['time'] = time[i]
        yield item

