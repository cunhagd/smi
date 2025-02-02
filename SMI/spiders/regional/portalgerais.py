import scrapy

class PortalgeraisSpider(scrapy.Spider):
    name = "Portal Gerais"
    ID = 165
    allowed_domains = ["portalgerais.com"]
    start_urls = ["https://portalgerais.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
