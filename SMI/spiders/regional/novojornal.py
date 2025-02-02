import scrapy

class NovojornalSpider(scrapy.Spider):
    name = "Novo Jornal"
    ID = 121
    allowed_domains = ["www.novojornal.com.br"]
    start_urls = ["https://www.novojornal.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
