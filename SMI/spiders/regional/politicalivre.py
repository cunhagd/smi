import scrapy

class PoliticalivreSpider(scrapy.Spider):
    name = "Política Livre"
    ID = 217
    allowed_domains = ["politicalivre.com.br"]
    start_urls = ["https://politicalivre.com.br/#gsc.tab=0"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
