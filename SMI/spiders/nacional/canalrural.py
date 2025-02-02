import scrapy

class CanalruralSpider(scrapy.Spider):
    name = "Canal Rural"
    ID = 54
    allowed_domains = ["www.canalrural.com.br"]
    start_urls = ["https://www.canalrural.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
