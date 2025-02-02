import scrapy

class G1_gdmgSpider(scrapy.Spider):
    name = "G1 Grande Minas"
    ID = 235
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/grande-minas/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
