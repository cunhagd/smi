import scrapy

class PioneirosSpider(scrapy.Spider):
    name = "Portal Pioneiros"
    ID = 135
    allowed_domains = ["portalpioneiros.fae.ufmg.br"]
    start_urls = ["https://portalpioneiros.fae.ufmg.br/artigos/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
