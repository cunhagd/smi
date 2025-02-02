import scrapy

class SbtSpider(scrapy.Spider):
    name = "SBT News"
    ID = 32
    allowed_domains = ["sbtnews.sbt.com.br"]
    start_urls = ["https://sbtnews.sbt.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
