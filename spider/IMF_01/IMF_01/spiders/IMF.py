# -*- coding: utf-8 -*-
import scrapy
from IMF_01.items import Imf01Item
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ImfSpider(scrapy.Spider):
    name = 'IMF'
    allowed_domains = ['imf.org']
    start_urls = ['http://data.imf.org/?sk=4C514D48-B6BA-49ED-8AB9-52B0C1A0179B&sId=1409151240976/']

    def parse(self, response):
        items = []
        print('1111111111111111111111111')
        urls_list = response.xpath("//a[@class='ShortListTitleDiv DisplayInline Clickable']/@href").extract()
        filename_list = response.xpath("//a[@class='ShortListTitleDiv DisplayInline Clickable']/text()").extract()
        print(urls_list)
        for i in range(0, len(urls_list)):
            print('2222222222222222222222')
            filename = "./Data/" + filename_list[i]
            print(filename)
            item = Imf01Item()
            item['urls'] = urls_list[i]
            item['filename'] = filename
            items.append(item)
        for item in items:
            yield scrapy.Request(url=item['urls'], mate={'mate_1': item}, callback=self.second_parse)

    def second_parse(self, response):
        item = response.mate['mate_1']
        content_list = response.xpath("//div[@class='PPTSCellConText']/text()").extract()
        content = ''
        for each in content_list:
            content += each
        item['content'] = content
        yield item