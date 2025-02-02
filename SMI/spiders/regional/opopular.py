import scrapy

class OpopularSpider(scrapy.Spider):
    name = "O Popular"
    ID = 119
    allowed_domains = ["opopularjm.com.br"]
    start_urls = ["https://opopularjm.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
