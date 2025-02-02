import scrapy
from datetime import datetime, timedelta
import sqlite3

class G1MgSpider(scrapy.Spider):
    name = "G1 Minas"
    ID = 7
    allowed_domains = ["g1.globo.com"]
    start_urls = ["https://g1.globo.com/mg/minas-gerais/"]

    def __init__(self, *args, **kwargs):
        super(G1MgSpider, self).__init__(*args, **kwargs)
        self.palavras_obrigatorias = self.carregar_palavras_chave(tipo='obrigatoria')
        self.palavras_adicionais = self.carregar_palavras_chave(tipo='adicional')
        self.logger.debug(f"Palavras obrigatórias carregadas: {self.palavras_obrigatorias}")
        self.logger.debug(f"Palavras adicionais carregadas: {self.palavras_adicionais}")
        self.noticias_filtradas = 0  # Inicializando a variável para contar notícias válidas

    def carregar_palavras_chave(self, tipo):
        """Carrega as palavras-chave do banco de dados."""
        conn = sqlite3.connect('db/banco_smi.db')
        cursor = conn.cursor()
        cursor.execute('SELECT palavra FROM palavras_chave WHERE tipo = ?', (tipo,))
        palavras = [row[0] for row in cursor.fetchall()]
        conn.close()
        return palavras

    def parse(self, response):
        # Calculando a data de ontem
        ontem = datetime.now() - timedelta(days=1)
        data_ontem = f"/{ontem.year:04}/{ontem.month:02}/{ontem.day:02}/"

        # Selecionando todos os links da página
        links_encontrados = response.css("a::attr(href)").getall()
        self.logger.debug(f"Total de links encontrados: {len(links_encontrados)}")

        links_filtrados = []

        for link in links_encontrados:
            if (
                data_ontem in link  # Verifica se a URL contém a data atual
                and "/esportes/" not in link
                and "/entretenimento/" not in link
            ):
                url_completa = response.urljoin(link)  # Ajusta URL relativa para absoluta
                links_filtrados.append(url_completa)
                yield scrapy.Request(url=url_completa, callback=self.parse_noticia)

        self.logger.debug(f"Total de links filtrados (notícias do dia): {len(links_filtrados)}")
        for link in links_filtrados:
            self.logger.debug(f"Notícia encontrada: {link}")

    def parse_noticia(self, response):
        # Usando o novo seletor para capturar o corpo da notícia
        corpo = " ".join(response.css('p.content-text__container::text').getall())

        # Extraindo o autor da notícia
        autor = response.css("p.content-publication-data__from::text").get()

        # Verificar se a notícia contém pelo menos 1 palavra obrigatória e 1 palavra adicional
        if self.verificar_palavras_chave(corpo):
            self.noticias_filtradas += 1  # Incrementa o contador de notícias filtradas
            self.logger.info(f"Notícia válida: {response.css('h1.content-head__title::text').get()}")
            self.logger.info(f"Autor da notícia: {autor}")  # Log para verificar o autor

            # Aqui você pode processar a notícia, como salvar no banco de dados ou retornar os dados
            yield {
                'titulo': response.css("h1.content-head__title::text").get(),
                'corpo': corpo,
                'autor': autor,  # Incluindo o autor no dicionário
                'link': response.url
            }
        else:
            self.logger.info(f"Notícia ignorada: {response.css('h1.content-head__title::text').get()}")

    def verificar_palavras_chave(self, corpo_noticia):
        """Verifica se o corpo da notícia contém pelo menos 1 palavra obrigatória e 1 palavra adicional."""
        corpo_noticia = corpo_noticia.lower().strip()  # Garantir que a comparação seja em minúsculas e sem espaços extras

        encontrou_obrigatoria = False
        palavras_adicionais_encontradas = []

        # Verificar se existe pelo menos 1 palavra obrigatória
        for palavra in self.palavras_obrigatorias:
            palavra = palavra.lower().strip()  # Garantir que as palavras também estão sem espaços extras
            if palavra in corpo_noticia:
                self.logger.debug(f"Palavra obrigatória encontrada: {palavra}")
                encontrou_obrigatoria = True
                break  # Não precisa verificar as outras palavras obrigatórias

        # Verificar se existem palavras adicionais
        for palavra in self.palavras_adicionais:
            palavra = palavra.lower().strip()  # Garantir que as palavras também estão sem espaços extras
            if palavra in corpo_noticia:
                palavras_adicionais_encontradas.append(palavra)

        # Log para indicar todas as palavras adicionais encontradas
        self.logger.debug(f"Palavras adicionais encontradas: {', '.join(palavras_adicionais_encontradas)}")

        # Retornar True se ambas as condições forem atendidas
        return encontrou_obrigatoria and len(palavras_adicionais_encontradas) > 0

    def closed(self, reason):
        """Este método é chamado quando o spider termina de rodar."""
        self.logger.info(f"Total de notícias válidas filtradas: {self.noticias_filtradas}")
