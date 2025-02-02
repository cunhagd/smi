import scrapy

class BrumadinhoSpider(scrapy.Spider):
    name = "Portal da Cidade (Brumadinho)"
    ID = 258
    allowed_domains = ["brumadinho.portaldacidade.com"]
    start_urls = ["https://brumadinho.portaldacidade.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
