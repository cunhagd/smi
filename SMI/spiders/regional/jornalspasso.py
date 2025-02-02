import scrapy

class JornalspassoSpider(scrapy.Spider):
    name = "Jornal SPasso"
    ID = 133
    allowed_domains = ["jornalspasso.com.br"]
    start_urls = ["https://jornalspasso.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
