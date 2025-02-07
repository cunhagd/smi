from scrapy.spiders import SitemapSpider
from datetime import datetime
from SMI.database import buscar_urls, buscar_apelido, buscar_pontos, buscar_abrangencia, buscar_categorias, seletor_autor, seletor_corpo, DB_PATH
from SMI.items import NoticiaItem
from SMI.utils import filtrar_keywords
import re


class EmSpider(SitemapSpider):
    name = "O Tempo"

    def __init__(self, *args, **kwargs):
        super(EmSpider, self).__init__(*args, **kwargs)
        apelidos = buscar_apelido(self.name)
        if apelidos:
            self.sitemap_urls = buscar_urls(DB_PATH, apelidos[0])
        else:
            print("Nenhum apelido encontrado no banco de dados.")
            self.sitemap_urls = []
        self.categorias_indesejadas = set(buscar_categorias())
        
        # Inicializa os contadores
        self.total_links_encontrados = 0
        self.total_ignoradas_categoria = 0
        self.total_ignoradas_data = 0
        self.total_ignoradas_palavras_chave = 0  # Contador para ignoradas por palavras-chave
        self.total_com_erro = 0
        self.total_relevantes_salvas = 0

    def obter_seletor(self, funcao_seletor, tipo):
        seletor = funcao_seletor(DB_PATH, self.name)
        if not seletor:
            self.log(f"Seletor CSS para {tipo} não encontrado para o portal '{self.name}'")
            return None
        return seletor

    def parse(self, response):
        current_timestamp = datetime.now().isoformat()
        today = datetime.now().date()

        # Incrementa o contador de links encontrados
        self.total_links_encontrados += 1

        # Ignora URLs com categorias indesejadas
        if any(categoria in response.url for categoria in self.categorias_indesejadas):
            self.logger.info(f"URL ignorada (categoria indesejada): {response.url}")
            self.total_ignoradas_categoria += 1
            return

        # Extrai o título da notícia
        title = response.xpath('//title/text()').get()
        if not title:
            title = response.xpath('//h1/text()').get()
        if not title:
            title = response.xpath('//meta[@property="og:title"]/@content').get()

        # Cria o objeto NoticiaItem
        item = NoticiaItem()
        item['title'] = title
        item['timestamp'] = current_timestamp
        item['url'] = response.url

        # Verifica se a notícia é de hoje
        news_date = datetime.fromisoformat(item["timestamp"]).date()
        if news_date != today:
            self.logger.info(f"Notícia ignorada (data: {news_date}): {response.url}")
            self.total_ignoradas_data += 1
            return

        # Obtém o seletor do corpo da notícia
        sel_corpo = self.obter_seletor(seletor_corpo, "corpo")
        if not sel_corpo:
            self.total_com_erro += 1
            return

        # Extrai o corpo completo da notícia
        paragrafos = response.css(sel_corpo).getall()
        corpo_completo = "\n".join([p.strip() for p in paragrafos if p.strip()])
        item['corpo_completo'] = corpo_completo

        # Filtra a notícia com base nas palavras-chave
        palavras_encontradas = filtrar_keywords(DB_PATH, corpo_completo, debug=True)
        if not palavras_encontradas:
            self.log(f"Notícia ignorada (não atende às palavras-chave): {response.url}")
            self.total_ignoradas_palavras_chave += 1  # Incrementa o contador correto
            return

        # Verifica a regra de relevância
        tem_obrigatoria = len(palavras_encontradas["obrigatorias"]) > 0
        tem_adicional = len(palavras_encontradas["adicionais"]) > 0
        if not (tem_obrigatoria and tem_adicional):
            self.log(f"Notícia ignorada (não atende à regra de relevância): {response.url}")
            self.total_ignoradas_palavras_chave += 1  # Incrementa o contador correto
            return

        # Adiciona as palavras-chave encontradas ao item
        item['palavras_obrigatorias_encontradas'] = palavras_encontradas["obrigatorias"]
        item['palavras_adicionais_encontradas'] = palavras_encontradas["adicionais"]

        # Obtém o seletor do autor
        sel_autor = self.obter_seletor(seletor_autor, "autor")
        if sel_autor:
            # Tenta capturar o autor em diferentes formatos
            autor = None

            # Função auxiliar para validar o texto do autor
            def is_valid_author(text):
                """
                Verifica se o texto do autor é válido.
                Um texto é considerado válido se não for vazio e não contiver caracteres especiais.
                """
                if not text or not isinstance(text, str):
                    return False
                # Define um padrão regex para identificar caracteres especiais
                # Permitimos letras, números, espaços e alguns caracteres comuns (ex.: hífen, apóstrofo)
                pattern = r"^[a-zA-Z0-9áéíóúÁÉÍÓÚãõÃÕçÇ\s\-']+$"
                return bool(re.match(pattern, text))

            # Caso 1: Autor dentro de um link (<a>)
            autor_link = response.css(f"{sel_autor} a::text").get()
            if autor_link and is_valid_author(autor_link.strip()):
                autor = autor_link.strip()

            # Caso 2: Autor como texto direto no elemento selecionado
            if not autor:
                autor_texto = response.css(f"{sel_autor}::text").get()
                if autor_texto and is_valid_author(autor_texto.strip()):
                    autor = autor_texto.strip()

            # Caso 3: Autor dentro de um <span> (ou outro elemento filho)
            if not autor:
                autor_span = response.css(f"{sel_autor} > span::text").get()
                if autor_span and is_valid_author(autor_span.strip()):
                    autor = autor_span.strip()

            # Caso 4: Autor em um atributo (ex.: title)
            if not autor:
                autor_title = response.css(f"{sel_autor}::attr(title)").get()
                if autor_title and is_valid_author(autor_title.strip()):
                    autor = autor_title.strip()

            # Define o autor como 'Redação O Tempo' se nenhum caso acima for satisfeito
            item['autor'] = autor if autor else 'Redação O Tempo'
        else:
            item['autor'] = 'Redação O Tempo'

        # Busca pontos e abrangência do portal
        pontos_portal = buscar_pontos(self.name)
        item['pontos'] = pontos_portal if pontos_portal else None
        abrangencia_portal = buscar_abrangencia(self.name)
        item['abrangencia'] = abrangencia_portal if abrangencia_portal else None

        # Incrementa o contador de notícias relevantes salvas
        self.total_relevantes_salvas += 1

        # Retorna o item da notícia
        yield item

    def closed(self, reason):
        # Exibe os resultados da depuração ao final da execução
        self.logger.info("=== Resumo da Execução ===")
        self.logger.info(f"Total de links de notícias encontrados: {self.total_links_encontrados}")
        self.logger.info(f"Total de notícias ignoradas por categoria: {self.total_ignoradas_categoria}")
        self.logger.info(f"Total de notícias ignoradas por data: {self.total_ignoradas_data}")
        self.logger.info(f"Total de notícias ignoradas por palavras-chave: {self.total_ignoradas_palavras_chave}")  # Contador correto
        self.logger.info(f"Total de notícias com erro: {self.total_com_erro}")
        self.logger.info(f"Total de notícias relevantes salvas: {self.total_relevantes_salvas}")