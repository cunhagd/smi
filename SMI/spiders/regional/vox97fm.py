import scrapy

class Vox97fmSpider(scrapy.Spider):
    name = "Vox 97 FM"
    ID = 223
    allowed_domains = ["vox97.com.br"]
    start_urls = ["https://vox97.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
