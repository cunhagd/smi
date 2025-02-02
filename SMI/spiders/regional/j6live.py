import scrapy

class J6liveSpider(scrapy.Spider):
    name = "J6 Live"
    ID = 132
    allowed_domains = ["j6live.com.br"]
    start_urls = ["https://j6live.com.br/?pl_eleicoes=false"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
