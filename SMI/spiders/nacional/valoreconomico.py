import scrapy

class ValoreconomicoSpider(scrapy.Spider):
    name = "Valor Econômico"
    ID = 250
    allowed_domains = ["valor.globo.com"]
    start_urls = ["https://valor.globo.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
