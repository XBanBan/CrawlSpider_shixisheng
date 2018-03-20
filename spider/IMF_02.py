#encoding=utf-8
from selenium import webdriver
from lxml import etree
import time

driver=webdriver.Firefox()
time.sleep(1)
driver.get("http://data.imf.org/?sk=4C514D48-B6BA-49ED-8AB9-52B0C1A0179B&sId=1409151240976")
time.sleep(10)
html = driver.page_source
etree_html = etree.HTML(html)
urls_list = etree_html.xpath("//a[@class='ShortListTitleDiv DisplayInline Clickable']/@href")
filename_list = etree_html.xpath("//a[@class='ShortListTitleDiv DisplayInline Clickable']/text()")
items = []
for i in range(0, len(urls_list)):
    driver.get(urls_list[i])
    time.sleep(15)
    item = driver.page_source
    etree_item = etree.HTML(item)
    content_list = etree_item.xpath("//div[@class='PPTSCellConText']/text()")
    content = ''
    for content_one in content_list:
        content = content + ";" + content_one
    items.append(content)
print(items)
