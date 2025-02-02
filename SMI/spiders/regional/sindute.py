import scrapy

class SinduteSpider(scrapy.Spider):
    name = "SindUTE"
    ID = 108
    allowed_domains = ["sindutemg.org.br"]
    start_urls = ["https://sindutemg.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
