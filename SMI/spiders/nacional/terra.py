import scrapy

class TerraSpider(scrapy.Spider):
    name = "Terra"
    ID = 25
    allowed_domains = ["www.terra.com.br"]
    start_urls = ["https://www.terra.com.br/ultimas/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
