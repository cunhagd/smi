import scrapy

class VhnewsSpider(scrapy.Spider):
    name = "VH News"
    ID = 102
    allowed_domains = ["vhnews.com.br"]
    start_urls = ["https://vhnews.com.br/?pl_eleicoes=false"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
