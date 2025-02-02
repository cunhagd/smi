import scrapy

class ManhacunewsSpider(scrapy.Spider):
    name = "Manhuaçu News"
    ID = 129
    allowed_domains = ["www.manhuacunews.com.br"]
    start_urls = ["https://www.manhuacunews.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
