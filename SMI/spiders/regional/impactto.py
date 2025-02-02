import scrapy

class ImpacttoSpider(scrapy.Spider):
    name = "Portal Impactto"
    ID = 156
    allowed_domains = ["portalimpactto.com.br"]
    start_urls = ["https://portalimpactto.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
