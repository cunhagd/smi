import scrapy

class AndradasSpider(scrapy.Spider):
    name = "Portal da Cidade (Andradas)"
    ID = 257
    allowed_domains = ["andradas.portaldacidade.com"]
    start_urls = ["https://andradas.portaldacidade.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
