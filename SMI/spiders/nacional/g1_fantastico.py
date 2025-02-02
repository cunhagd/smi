import scrapy

class G1_fantasticoSpider(scrapy.Spider):
    name = "Fantástico"
    ID = 10
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/fantastico/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
