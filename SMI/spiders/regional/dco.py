import scrapy

class DcoSpider(scrapy.Spider):
    name = "Diário Causa Operária"
    ID = 181
    allowed_domains = ["causaoperaria.org.br"]
    start_urls = ["https://causaoperaria.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
