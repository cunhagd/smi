import scrapy

class BloghpSpider(scrapy.Spider):
    name = "Blog do HP"
    ID = 220
    allowed_domains = ["www.blogdohp.com"]
    start_urls = ["https://www.blogdohp.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
