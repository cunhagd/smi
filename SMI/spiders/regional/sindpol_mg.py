import scrapy

class Sindpol_mgSpider(scrapy.Spider):
    name = "Sindpol MG"
    ID = 256
    allowed_domains = ["htps:"]
    start_urls = ["htps://sindpolmg.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
