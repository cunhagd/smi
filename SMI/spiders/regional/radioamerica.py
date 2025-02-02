import scrapy

class RadioamericaSpider(scrapy.Spider):
    name = "Rádio América"
    ID = 80
    allowed_domains = ["radioamerica.arquidiocesebh.org.br"]
    start_urls = ["https://radioamerica.arquidiocesebh.org.br/noticias/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
