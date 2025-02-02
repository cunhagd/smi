import scrapy

class ConexaoitajubaSpider(scrapy.Spider):
    name = "Conexão Itajuba"
    ID = 195
    allowed_domains = ["conexaoitajuba.com.br"]
    start_urls = ["https://conexaoitajuba.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
