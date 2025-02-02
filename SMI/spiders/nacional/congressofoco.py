import scrapy

class CongressofocoSpider(scrapy.Spider):
    name = "Congresso em Foco"
    ID = 52
    allowed_domains = ["congressoemfoco.uol.com.br"]
    start_urls = ["https://congressoemfoco.uol.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
