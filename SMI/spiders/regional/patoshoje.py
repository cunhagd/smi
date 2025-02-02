import scrapy

class PatoshojeSpider(scrapy.Spider):
    name = "Patos Hoje"
    ID = 111
    allowed_domains = ["patoshoje.com.br"]
    start_urls = ["https://patoshoje.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
