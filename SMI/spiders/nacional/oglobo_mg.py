import scrapy

class Oglobo_mgSpider(scrapy.Spider):
    name = "Portal O Globo"
    ID = 12
    allowed_domains = ["oglobo.globo.com"]
    start_urls = ["https://oglobo.globo.com/brasil/minas-gerais/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
