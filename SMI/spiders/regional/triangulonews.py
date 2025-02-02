import scrapy

class TriangulonewsSpider(scrapy.Spider):
    name = "Triângulo News"
    ID = 97
    allowed_domains = ["triangulonews.com.br"]
    start_urls = ["https://triangulonews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
