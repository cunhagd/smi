import scrapy

class JornalclassivaleSpider(scrapy.Spider):
    name = "Jornal Classivale"
    ID = 197
    allowed_domains = ["jornalclassivale.com.br"]
    start_urls = ["https://jornalclassivale.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
