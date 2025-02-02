import scrapy

class MauaagoraSpider(scrapy.Spider):
    name = "Mauá Agora"
    ID = 128
    allowed_domains = ["mauaagora.com.br"]
    start_urls = ["https://mauaagora.com.br/category/noticiais/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
