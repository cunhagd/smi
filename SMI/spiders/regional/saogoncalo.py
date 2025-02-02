import scrapy

class SaogoncaloSpider(scrapy.Spider):
    name = "São Gonçalo Agora"
    ID = 95
    allowed_domains = ["www.saogoncaloagora.com.br"]
    start_urls = ["https://www.saogoncaloagora.com.br/?pl_eleicoes=false"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
