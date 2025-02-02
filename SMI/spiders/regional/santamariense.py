import scrapy

class SantamarienseSpider(scrapy.Spider):
    name = "Plantão Santamariense"
    ID = 115
    allowed_domains = ["plantaosantamariense.com.br"]
    start_urls = ["https://plantaosantamariense.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
