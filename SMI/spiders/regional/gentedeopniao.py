import scrapy

class GentedeopniaoSpider(scrapy.Spider):
    name = "Gente de Opnião"
    ID = 164
    allowed_domains = ["www.gentedeopiniao.com.br"]
    start_urls = ["https://www.gentedeopiniao.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
