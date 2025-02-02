import scrapy

class G1_jnSpider(scrapy.Spider):
    name = "Jornal Nacional"
    ID = 11
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/jornal-nacional/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
