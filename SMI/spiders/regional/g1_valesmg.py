import scrapy

class G1_valesmgSpider(scrapy.Spider):
    name = "G1 Vales de MG"
    ID = 238
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/vales-mg/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
