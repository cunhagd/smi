import scrapy
from datetime import datetime
from SMI.helpers.db_helper import carregar_palavras_chave, obter_pontos_portal, salvar_noticia
from SMI.helpers.keywords_helper import verificar_palavras_chave
from SMI.helpers.scraping_helper import calcular_data_hoje, extrair_texto, limpar_autor

class G1MgSpider(scrapy.Spider):
    name = "G1 Minas"
    ID = 7
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/minas-gerais/"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.palavras_obrigatorias = carregar_palavras_chave(tipo='obrigatoria')
        self.palavras_adicionais = carregar_palavras_chave(tipo='adicional')
        self.logger.debug(f"Palavras obrigatórias: {self.palavras_obrigatorias}")
        self.logger.debug(f"Palavras adicionais: {self.palavras_adicionais}")
        self.noticias_filtradas = 0

    def parse(self, response):
        data_hoje = calcular_data_hoje()
        links_encontrados = response.css("a::attr(href)").getall()
        links_filtrados = [response.urljoin(link) for link in links_encontrados if data_hoje in link and "/esportes/" not in link and "/entretenimento/" not in link]

        self.logger.debug(f"Links filtrados: {len(links_filtrados)}")
        for link in links_filtrados:
            yield scrapy.Request(url=link, callback=self.parse_noticia)

    def parse_noticia(self, response):
        corpo = " ".join(response.css('p.content-text__container::text').getall())
        autor = limpar_autor(response.css("a.multi_signatures::text").get())
        titulo = extrair_texto(response, "h1.content-head__title::text")
        link = response.url
        data = datetime.now().strftime("%Y-%m-%d")
        
        # Verificando palavras-chave
        valido, palavras_obrigatorias_encontradas, palavras_adicionais_encontradas = verificar_palavras_chave(corpo, self.palavras_adicionais, self.palavras_obrigatorias)
        
        if valido:
            self.noticias_filtradas += 1
            self.logger.info(f"Notícia válida: {titulo}")
            pontos = obter_pontos_portal(self.ID)
            salvar_noticia(data, "G1 Minas", titulo, corpo, link, autor, pontos, palavras_adicionais_encontradas, palavras_obrigatorias_encontradas)
        else:
            palavras_faltando = set(self.palavras_obrigatorias) - set(palavras_obrigatorias_encontradas)
            self.logger.info(f"Notícia ignorada: {titulo}, palavras faltando: {', '.join(palavras_faltando)}")
