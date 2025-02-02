import scrapy

class EmSpider(scrapy.Spider):
    name = "Estado de Minas"
    ID = 83
    allowed_domains = ["www.em.com.br"]
    start_urls = ["https://www.em.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
