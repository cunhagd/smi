import scrapy

class BlogpedlowskiSpider(scrapy.Spider):
    name = "Blog Pedlowski"
    ID = 218
    allowed_domains = ["blogdopedlowski.com"]
    start_urls = ["https://blogdopedlowski.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
