import scrapy

class JornalfloripaSpider(scrapy.Spider):
    name = "Jornal Floripa"
    ID = 139
    allowed_domains = ["jornalfloripa.com.br"]
    start_urls = ["https://jornalfloripa.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
