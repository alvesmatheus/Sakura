import scrapy

from crawlers.spiders.selectors import sakura_cards_selectors as ccs
from crawlers.loaders import SakuraCardLoader
from crawlers.items import SakuraCardItem

class SakuraCardsSpider(scrapy.Spider):
    name = 'sakura-cards'
    start_urls = ['https://ccsakura.fandom.com/wiki/Clow_Cards']

    def parse(self, response):
        metadata = {'card_type': 'Sakura Card'}
        card_urls = response.xpath(ccs.CARD_PAGE).getall()
        
        for url in card_urls:
            yield response.follow(url=url, callback=self.parse_card, meta=metadata)
    
    def parse_card(self, response):
        loader = SakuraCardLoader(item=SakuraCardItem(), response=response)

        loader.add_xpath('card', ccs.NAME)
        loader.add_value('card_type', response.meta.get('card_type'))
        loader.add_xpath('img_url', ccs.IMAGE_URL)
        loader.add_xpath('sign', ccs.SIGN)
        loader.add_xpath('hierarchy', ccs.HIEGHERARCHY)
        loader.add_xpath('magic_type', ccs.MAGIC_TYPE)

        return loader.load_item()