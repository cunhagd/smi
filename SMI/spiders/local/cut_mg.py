import scrapy

class Cut_mgSpider(scrapy.Spider):
    name = "CUT (MG)"
    ID = 78
    allowed_domains = ["mg.cut.org.br"]
    start_urls = ["https://mg.cut.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
