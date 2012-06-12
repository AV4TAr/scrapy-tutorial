from scrapy.contrib.linkextractors.sgml     import SgmlLinkExtractor
from scrapy.contrib.spiders                 import CrawlSpider, Rule

from scrapy.selector                        import HtmlXPathSelector 

class Dinet2Spider(CrawlSpider):

    name = "dinet2"
    allowed_domains = ["di.net"]
    start_urls = [
        "http://www.di.net/almanac/firms/",
    ]

    rules = (

            Rule(SgmlLinkExtractor(allow=r'(^http://www.di.net/almanac/firms/page[0-9]*)$',
                                   canonicalize = True),
                        follow = True,
                        callback = 'parse_page'),

            Rule(SgmlLinkExtractor (allow=r'^http://www.di.net/almanac/firms/(.*)',
                                   canonicalize = True),
                        follow = False,
                        callback = 'parse_firm'),

        )

    def parse_page(self, response):
        print 'parse_page: ' + response.url


    def parse_firm(self, response):
        print 'parse_firm: ' + response.url
