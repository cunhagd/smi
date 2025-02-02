import scrapy

class SindsaudeSpider(scrapy.Spider):
    name = "Sind-Saúde (MG)"
    ID = 191
    allowed_domains = ["sindsaudemg.org.br"]
    start_urls = ["https://sindsaudemg.org.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
