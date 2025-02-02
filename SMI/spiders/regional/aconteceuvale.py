import scrapy

class AconteceuvaleSpider(scrapy.Spider):
    name = "Aconteceu no Vale"
    ID = 213
    allowed_domains = ["aconteceunovale.com.br"]
    start_urls = ["https://aconteceunovale.com.br/portal/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
