import scrapy

class FmjequitibaSpider(scrapy.Spider):
    name = "Cidade FM Jequitibá"
    ID = 260
    allowed_domains = ["www.cidadefmjequitiba.com.br"]
    start_urls = ["https://www.cidadefmjequitiba.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
