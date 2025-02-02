import scrapy

class CidadeipatingaSpider(scrapy.Spider):
    name = "Portal Cidade Ipatinga"
    ID = 248
    allowed_domains = ["ipatinga.portaldacidade.com"]
    start_urls = ["https://ipatinga.portaldacidade.com/noticias"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
