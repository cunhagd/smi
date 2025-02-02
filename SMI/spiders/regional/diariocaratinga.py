import scrapy

class DiariocaratingaSpider(scrapy.Spider):
    name = "Diário de Caratinga"
    ID = 243
    allowed_domains = ["diariodecaratinga.com.br"]
    start_urls = ["https://diariodecaratinga.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
