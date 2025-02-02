import scrapy

class VejaSpider(scrapy.Spider):
    name = "Veja Abril"
    ID = 21
    allowed_domains = ["veja.abril.com.br"]
    start_urls = ["https://veja.abril.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
