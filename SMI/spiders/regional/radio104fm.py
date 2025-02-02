import scrapy

class Radio104fmSpider(scrapy.Spider):
    name = "Rádio 104 FM"
    ID = 225
    allowed_domains = ["104fm.net.br"]
    start_urls = ["https://104fm.net.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
