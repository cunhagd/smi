import scrapy

class MaistopnewsSpider(scrapy.Spider):
    name = "Mais Top News"
    ID = 130
    allowed_domains = ["maistopnews.com.br"]
    start_urls = ["https://maistopnews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
