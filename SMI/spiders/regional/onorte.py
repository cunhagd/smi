import scrapy

class OnorteSpider(scrapy.Spider):
    name = "Jornal O Norte"
    ID = 137
    allowed_domains = ["onorte.net"]
    start_urls = ["https://onorte.net/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
