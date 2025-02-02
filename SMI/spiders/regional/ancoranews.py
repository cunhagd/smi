import scrapy

class AncoranewsSpider(scrapy.Spider):
    name = "Âncora News"
    ID = 207
    allowed_domains = ["ancoranews.com.br"]
    start_urls = ["http://ancoranews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
