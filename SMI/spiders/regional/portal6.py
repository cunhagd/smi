import scrapy

class Portal6Spider(scrapy.Spider):
    name = "Portal 6"
    ID = 62
    allowed_domains = ["portal6.com.br"]
    start_urls = ["https://portal6.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
