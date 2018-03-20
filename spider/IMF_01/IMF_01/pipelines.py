# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Imf01Pipeline(object):
    def process_item(self, item, spider):
        filename = item['filename']
        filename += ".txt"
        fp = open(filename, "w")
        fp.write(item['content'])
        fp.close()

        return item