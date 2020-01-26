CARD_PAGE = '//div[@class="lightbox-caption"]/a/@href'

NAME = '//*[@id="PageHeader"]/div[1]/h1/text()'

IMAGE_URL = '//*[@id="pi-tab-1"]/figure/a/img/@src'

SIGN = '//*[@id="mw-content-text"]/aside/div[2]/div/a/text()'

# This doesn't match anything, but leaving it here for historical purposes
HIEGHERARCHY = '//table[@class="infobox"]//tr[4]//a/text() | //table[@class="infobox"]//tr[4]/td[2]/text()'

MAGIC_TYPE = '//*[@id="mw-content-text"]/aside/div[3]/div/text()'