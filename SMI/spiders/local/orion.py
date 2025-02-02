import scrapy

class OrionSpider(scrapy.Spider):
    name = "Blog do Orion"
    ID = 73
    allowed_domains = ["www.blogdoorion.com.br"]
    start_urls = ["https://www.blogdoorion.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
