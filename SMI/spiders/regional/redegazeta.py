import scrapy

class RedegazetaSpider(scrapy.Spider):
    name = "Rede Gazeta"
    ID = 106
    allowed_domains = ["www.redegazeta.com.br"]
    start_urls = ["https://www.redegazeta.com.br/noticias/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
