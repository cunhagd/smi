import scrapy

class JornalagoraSpider(scrapy.Spider):
    name = "Jornal Agora"
    ID = 148
    allowed_domains = ["www.agoracomvoce.com.br"]
    start_urls = ["https://www.agoracomvoce.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
