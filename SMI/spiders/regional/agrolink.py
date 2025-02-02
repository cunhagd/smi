import scrapy

class AgrolinkSpider(scrapy.Spider):
    name = "Agrolink"
    ID = 212
    allowed_domains = ["www.agrolink.com.br"]
    start_urls = ["https://www.agrolink.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
