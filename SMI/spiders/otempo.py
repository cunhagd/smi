from scrapy.spiders import SitemapSpider
from datetime import datetime
from SMI.database import buscar_urls, buscar_apelido, buscar_pontos, buscar_abrangencia, buscar_categorias, seletor_autor, seletor_corpo, DB_PATH
from SMI.items import NoticiaItem
from SMI.utils import filtrar_keywords


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

    def obter_seletor(self, funcao_seletor, tipo):
        seletor = funcao_seletor(DB_PATH, self.name)
        if not seletor:
            self.log(f"Seletor CSS para {tipo} não encontrado para o portal '{self.name}'")
            return None
        return seletor

    def parse(self, response):
        current_timestamp = datetime.now().isoformat()
        today = datetime.now().date()

        # Ignora URLs com categorias indesejadas
        if any(categoria in response.url for categoria in self.categorias_indesejadas):
            self.logger.info(f"URL ignorada (categoria indesejada): {response.url}")
            return

        # Extrai o título da notícia
        title = response.xpath('//title/text()').get()
        if not title:
            title = response.xpath('//h1/text()').get()
        if not title:
            title = response.xpath('//meta[@property="og:title"]/@content').get()

        # Verifica se a notícia é de hoje
        news_date = datetime.fromisoformat(item["timestamp"]).date()
        if news_date != today:
            self.logger.info(f"Notícia ignorada (data: {news_date}): {response.url}")
            return

        # Obtém o seletor do corpo da notícia
        sel_corpo = self.obter_seletor(seletor_corpo, "corpo")
        if not sel_corpo:
            return

        # Extrai o corpo completo da notícia
        paragrafos = response.css(sel_corpo).getall()
        corpo_completo = "\n".join([p.strip() for p in paragrafos if p.strip()])
        item['corpo_completo'] = corpo_completo

        # Filtra a notícia com base nas palavras-chave
        palavras_encontradas = filtrar_keywords(DB_PATH, corpo_completo, debug=True)
        if not palavras_encontradas:
            self.log(f"Notícia ignorada (não atende às palavras-chave): {response.url}")
            return

        # Verifica a regra de relevância
        tem_obrigatoria = len(palavras_encontradas["obrigatorias"]) > 0
        tem_adicional = len(palavras_encontradas["adicionais"]) > 0
        if not (tem_obrigatoria and tem_adicional):
            self.log(f"Notícia ignorada (não atende à regra de relevância): {response.url}")
            return

        # Adiciona as palavras-chave encontradas ao item
        item['palavras_obrigatorias_encontradas'] = palavras_encontradas["obrigatorias"]
        item['palavras_adicionais_encontradas'] = palavras_encontradas["adicionais"]

        # Obtém o seletor do autor
        sel_autor = self.obter_seletor(seletor_autor, "autor")
        if sel_autor:
            # Verifica se existe um link (<a>) dentro do seletor do autor
            autor_link = response.css(f"{sel_autor} a::text").get()
            if autor_link:
                # Caso 2: Autor está dentro de um link
                autor = autor_link.strip()
            else:
                # Caso 1: Autor é um texto fixo (ex.: "Canal O TEMPO")
                autor = response.css(f"{sel_autor} > span::text").get()
                autor = autor.strip() if autor else None

            item['autor'] = autor
        else:
            item['autor'] = "Redação O Tempo"

        # Busca pontos e abrangência do portal
        pontos_portal = buscar_pontos(self.name)
        item['pontos'] = pontos_portal if pontos_portal else None

        abrangencia_portal = buscar_abrangencia(self.name)
        item['abrangencia'] = abrangencia_portal if abrangencia_portal else None

        # Cria o objeto NoticiaItem
        item = NoticiaItem()
        item['title'] = title
        item['timestamp'] = current_timestamp
        item['url'] = response.url
        item['corpo_completo'] = corpo_completo
        item['palavras_obrigatorias_encontradas'] = palavras_encontradas["obrigatorias"]
        item['palavras_adicionais_encontradas'] = palavras_encontradas["adicionais"]
        item['autor'] = autor
        item['pontos'] = pontos_portal
        item['abrangencia'] = abrangencia_portal

        # Retorna o item da notícia
        yield item