import scrapy

class ImparcialnewsSpider(scrapy.Spider):
    name = "Imparcial News"
    ID = 155
    allowed_domains = ["imparcialnews.com.br"]
    start_urls = ["https://imparcialnews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
