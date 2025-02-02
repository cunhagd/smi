import scrapy

class Itatiaia_jfSpider(scrapy.Spider):
    name = "Itatiaia Juiz de Fora"
    ID = 241
    allowed_domains = ["radioitatiaiajf.com.br"]
    start_urls = ["https://radioitatiaiajf.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
