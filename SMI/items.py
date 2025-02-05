import scrapy

class NoticiaItem(scrapy.Item):
    title = scrapy.Field()
    timestamp = scrapy.Field()
    url = scrapy.Field()
    corpo_completo = scrapy.Field()
    palavras_obrigatorias_encontradas = scrapy.Field()
    palavras_adicionais_encontradas = scrapy.Field()
    autor = scrapy.Field()
    pontos = scrapy.Field()
    abrangencia = scrapy.Field()