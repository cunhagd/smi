import sqlite3  # Ou outro banco de dados de sua escolha

class SaveToDatabasePipeline:
    def __init__(self):
        # Conectar ao banco de dados (ou criar se não existir)
        self.conn = sqlite3.connect("news.db")
        self.cursor = self.conn.cursor()
        # Criar tabela se ela ainda não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS noticias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                titulo TEXT,
                corpo TEXT,
                link TEXT,
                autor TEXT,
                abrangencia TEXT,
                pontos INTEGER,
                adicionais TEXT,
                obrigatorio TEXT,
            )
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        # Inserir os dados no banco de dados
        self.cursor.execute("""
            INSERT INTO noticias (timestamp, title, corpo_completo, url, autor, corpo_completo)
            VALUES (?, ?, ?, ?, ?)
        """, (
            item.get("title"),
            item.get("timestamp"),
            item.get("url"),
            item.get("autor"),
            item.get("corpo_completo")
        ))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # Fechar a conexão com o banco de dados quando o spider terminar
        self.conn.close()