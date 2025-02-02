import scrapy

class G1_trianguloSpider(scrapy.Spider):
    name = "G1 Triângulo Mineiro"
    ID = 237
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/triangulo-mineiro/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
