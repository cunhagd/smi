import scrapy

class VozdopovoSpider(scrapy.Spider):
    name = "A Voz do Povo"
    ID = 205
    allowed_domains = ["avozdopovo.org"]
    start_urls = ["https://avozdopovo.org/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
