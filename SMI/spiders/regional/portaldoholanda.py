import scrapy

class PortaldoholandaSpider(scrapy.Spider):
    name = "Portal de Holanda"
    ID = 159
    allowed_domains = ["www.portaldoholanda.com.br"]
    start_urls = ["https://www.portaldoholanda.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
