import scrapy

class ClowCardItem(scrapy.Item):
    card = scrapy.Field()
    card_type = scrapy.Field()
    img_url = scrapy.Field()
    sign = scrapy.Field()
    hierarchy = scrapy.Field()
    magic_type = scrapy.Field()

class SakuraCardItem(scrapy.Item):
    card = scrapy.Field()
    card_type = scrapy.Field()
    img_url = scrapy.Field()
    sign = scrapy.Field()
    hierarchy = scrapy.Field()
    magic_type = scrapy.Field()