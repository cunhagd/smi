import scrapy

class Jovempan_mgSpider(scrapy.Spider):
    name = "Jovem Pan MG"
    ID = 40
    allowed_domains = ["jovempan.com.br"]
    start_urls = ["https://jovempan.com.br/tag/minas-gerais"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
