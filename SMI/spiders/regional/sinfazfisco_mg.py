import scrapy

class Sinfazfisco_mgSpider(scrapy.Spider):
    name = "SinfazFisco"
    ID = 72
    allowed_domains = ["sinfazfiscomg.org.br"]
    start_urls = ["https://sinfazfiscomg.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
