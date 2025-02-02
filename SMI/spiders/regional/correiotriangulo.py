import scrapy

class CorreiotrianguloSpider(scrapy.Spider):
    name = "Correio do Triângulo"
    ID = 170
    allowed_domains = ["www.correiodotriangulo.com.br"]
    start_urls = ["https://www.correiodotriangulo.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
