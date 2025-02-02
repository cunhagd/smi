import scrapy

class ParacatunewsSpider(scrapy.Spider):
    name = "Paracatu News"
    ID = 113
    allowed_domains = ["paracatunews.com.br"]
    start_urls = ["https://paracatunews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
