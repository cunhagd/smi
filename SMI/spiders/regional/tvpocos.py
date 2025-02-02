import scrapy

class TvpocosSpider(scrapy.Spider):
    name = "TV Poços"
    ID = 228
    allowed_domains = ["tvpocos.com.br"]
    start_urls = ["https://tvpocos.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
