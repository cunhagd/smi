import scrapy

class DiariogoiasSpider(scrapy.Spider):
    name = "Diário de Góias"
    ID = 187
    allowed_domains = ["diariodegoias.com.br"]
    start_urls = ["https://diariodegoias.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
