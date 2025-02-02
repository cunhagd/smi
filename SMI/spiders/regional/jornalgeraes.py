import scrapy

class JornalgeraesSpider(scrapy.Spider):
    name = "Jornal Geraes(Portal Galilé)"
    ID = 172
    allowed_domains = ["jornalgeraes.com.br"]
    start_urls = ["https://jornalgeraes.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
