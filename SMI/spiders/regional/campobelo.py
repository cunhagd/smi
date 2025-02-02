import scrapy

class CampobeloSpider(scrapy.Spider):
    name = "Campo Belo em Foco"
    ID = 171
    allowed_domains = ["www.campobeloemfoco.com.br"]
    start_urls = ["https://www.campobeloemfoco.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
