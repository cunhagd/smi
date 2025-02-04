import sqlite3
import db.automate.dic as dic # Importando o módulo dic.py onde estão os dados dos portais

# Função para inserir dados na tabela 'portais'
def inserir_dados():
    # Caminho do banco de dados
    db_path = r'db\banco_smi.db'
    
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Iterar sobre os portais do dic.py
    for apelido, portal in dic.portais.items():
        # Montar o dicionário com os dados a serem inseridos
        dados = {
            'apelido': apelido,          # Usando a chave do dicionário como apelido
            'nome': portal['nome'],
            'url': portal['url'],
            'rastreio': "",
            'tipo': "",
            'abrangencia': portal['abrangencia'],
            'prioridade': portal['prioridade'],
            'pontos': portal['pontos']
        }
        
        # Comando SQL para inserir os dados
        sql = '''
        INSERT INTO portais (apelido, nome, url, rastreio, tipo, abrangencia, prioridade, pontos)
        VALUES (:apelido, :nome, :url, :rastreio, :tipo, :abrangencia, :prioridade, :pontos)
        '''
        
        try:
            # Executando a inserção dos dados
            cursor.execute(sql, dados)
            
            # Commitando as alterações para salvar no banco
            conn.commit()
            
            print(f"Dados inseridos com sucesso para o portal {apelido}")
        
        except sqlite3.IntegrityError as e:
            # Captura de erros relacionados à integridade (ex: URL única)
            print(f"Erro de integridade ao inserir o portal {apelido}: {e}")
        
        except Exception as e:
            # Captura de outros erros
            print(f"Erro ao inserir dados do portal {apelido}: {e}")
    
    # Fechar a conexão com o banco
    cursor.close()
    conn.close()

# Chamando a função para inserir os dados
if __name__ == "__main__":
    inserir_dados()
