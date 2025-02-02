import scrapy

class RadioinconfidenciaSpider(scrapy.Spider):
    name = "Rádio Inconfidência"
    ID = 81
    allowed_domains = ["www.inconfidencia.com.br"]
    start_urls = ["https://www.inconfidencia.com.br/noticias/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
