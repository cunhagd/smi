import scrapy

class G1_sulmgSpider(scrapy.Spider):
    name = "G1 Sul de Minas"
    ID = 236
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/sul-de-minas/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
