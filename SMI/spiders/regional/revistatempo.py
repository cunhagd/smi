import scrapy

class RevistatempoSpider(scrapy.Spider):
    name = "Revista Tempo"
    ID = 91
    allowed_domains = ["revistatempo.com.br"]
    start_urls = ["https://revistatempo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
