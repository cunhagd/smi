import scrapy

class JcnoticiasSpider(scrapy.Spider):
    name = "JC Notícias"
    ID = 244
    allowed_domains = ["www.jcnoticias.com.br"]
    start_urls = ["https://www.jcnoticias.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
