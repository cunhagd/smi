import scrapy

class WebterraSpider(scrapy.Spider):
    name = "Web Terra"
    ID = 103
    allowed_domains = ["webterra.com.br"]
    start_urls = ["https://webterra.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
