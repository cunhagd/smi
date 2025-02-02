import scrapy

class MirantebocainaSpider(scrapy.Spider):
    name = "Mirante da Bocaina"
    ID = 124
    allowed_domains = ["www.mirantedabocaina.com.br"]
    start_urls = ["https://www.mirantedabocaina.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
