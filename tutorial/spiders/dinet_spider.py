from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector 

from tutorial.items import DiItem


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.di.net/almanac/firms/",
    ]

    def parse(self, response):
	hxs = HtmlXPathSelector(response)
        sites = hxs.select('//html/body/div[2]/div/div[2]/table/tbody/tr')
        items = []

        for site in sites:
            item = CompanyItem()
            #item['title']  = site.select('a/text()').extract()
            #item['link'] = site.select('a/@href').extract()
            #item['desc'] = site.select('text()').extract()
            items.append(item)

        return items
