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

        # Extraindo o autor da notícia (novo seletor)
        autor = response.css("a.multi_signatures::text").get()

        # Verificar se o autor contém "Por" no início e removê-lo
        if autor:
            autor = autor.strip()
            if autor.lower().startswith("por "):  # Verifica se começa com "Por"
                autor = autor[3:].strip()  # Remove "Por"
        else:
            autor = "Autor não encontrado"

        # Definindo a data como a data atual
        data_atual = datetime.now().strftime("%Y-%m-%d")  # Formato YYYY-MM-DD

        # Verificar se a notícia contém pelo menos 1 palavra obrigatória e 1 palavra adicional
        palavras_adicionais_encontradas = []
        if self.verificar_palavras_chave(corpo, palavras_adicionais_encontradas):
            self.noticias_filtradas += 1  # Incrementa o contador de notícias filtradas
            self.logger.info(f"Notícia válida: {response.css('h1.content-head__title::text').get()}")
            self.logger.info(f"Autor da notícia: {autor}")  # Log para verificar o autor

            # Salvando no banco de dados
            self.salvar_noticia(
                titulo=response.css("h1.content-head__title::text").get(),
                corpo=corpo,
                autor=autor,
                data=data_atual,
                link=response.url,
                palavras_adicionais=palavras_adicionais_encontradas
            )
        else:
            self.logger.info(f"Notícia ignorada: {response.css('h1.content-head__title::text').get()}")

    def verificar_palavras_chave(self, corpo_noticia, palavras_adicionais_encontradas):
        """Verifica se o corpo da notícia contém pelo menos 1 palavra obrigatória e 1 palavra adicional."""
        corpo_noticia = corpo_noticia.lower().strip()  # Garantir que a comparação seja em minúsculas e sem espaços extras

        encontrou_obrigatoria = False

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

    def salvar_noticia(self, titulo, corpo, autor, data, link, palavras_adicionais):
        """Salva a notícia no banco de dados, incluindo o valor dos pontos do portal."""
        # Conectando ao banco de dados
        conn = sqlite3.connect('db/banco_smi.db')
        cursor = conn.cursor()

        # Passo 1: Buscar o valor de pontos do portal na tabela portais
        cursor.execute("SELECT pontos FROM portais WHERE id = ?", (self.ID,))
        resultado = cursor.fetchone()

        # Passo 2: Verificar se o resultado foi encontrado e obter o valor de pontos
        if resultado:
            pontos = resultado[0]  # Extrai o valor da coluna "pontos"
        else:
            pontos = 0  # Se não encontrar, podemos atribuir 0 pontos como padrão

        # Passo 3: Inserir a notícia na tabela "noticias" com o valor de pontos
        cursor.execute("""
            INSERT INTO noticias (data, portal, titulo, corpo, link, autor, pontos, keywords)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (data, "G1 Minas", titulo, corpo, link, autor, pontos, ', '.join(palavras_adicionais)))

        # Commit e fechamento da conexão
        conn.commit()
        conn.close()


