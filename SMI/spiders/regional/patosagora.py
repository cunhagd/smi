import scrapy

class PatosagoraSpider(scrapy.Spider):
    name = "Patos Agora"
    ID = 112
    allowed_domains = ["patosagora.net"]
    start_urls = ["https://patosagora.net/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
