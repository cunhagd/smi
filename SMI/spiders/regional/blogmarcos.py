import scrapy

class BlogmarcosSpider(scrapy.Spider):
    name = "Blog do Marcos Almeida"
    ID = 219
    allowed_domains = ["marcosalmeidalocutor.wordpress.com"]
    start_urls = ["https://marcosalmeidalocutor.wordpress.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
