import scrapy

class Asthe_mgSpider(scrapy.Spider):
    name = "Asthe MG"
    ID = 209
    allowed_domains = ["asthemg.org.br"]
    start_urls = ["https://asthemg.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
