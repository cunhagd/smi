import scrapy

class JovempanSpider(scrapy.Spider):
    name = "Jovem Pan"
    ID = 41
    allowed_domains = ["jovempan.com.br"]
    start_urls = ["https://jovempan.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
