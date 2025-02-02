import scrapy

class MultisomSpider(scrapy.Spider):
    name = "MultiSom Cataguases"
    ID = 126
    allowed_domains = ["multisomcataguases.com"]
    start_urls = ["https://multisomcataguases.com/noticias/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
