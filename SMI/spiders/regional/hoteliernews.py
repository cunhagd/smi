import scrapy

class HoteliernewsSpider(scrapy.Spider):
    name = "Portal Hotelier News"
    ID = 157
    allowed_domains = ["www.hoteliernews.com.br"]
    start_urls = ["https://www.hoteliernews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
