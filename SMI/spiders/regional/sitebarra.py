import scrapy

class SitebarraSpider(scrapy.Spider):
    name = "Site Barra"
    ID = 71
    allowed_domains = ["sitebarra.com.br"]
    start_urls = ["https://sitebarra.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
