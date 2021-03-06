# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    title = Field()
    link = Field()
    description = Field()
    pass

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class CompanyItem(Item):
    rank = Field()
    address = Field()
    phone = Field()
    website = Field()
    ww_revenue = Field()
    us_revenue = Field()
    ww_staff = Field()
    us_staff = Field()
    headquarters = Field()
    year_established = Field()
