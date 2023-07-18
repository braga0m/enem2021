#pacotes
import pandas as pd
import sqlite3

#importando os dados do ENEM
dados = pd.read_csv('C:/Users/Matias/Documents/Projetos_e_Estudos/ENEM_2021/DADOS/ENEM_2021_sem_treineiros.csv',
                    encoding='UTF-8', sep = ',')

dados.head(10)

#criando uma conexão sqlite
conn = sqlite3.connect('ENEM_2021_sem_treineiros.db')

#importando para o db
dados.to_sql(name = 'ENEM_2021', con = conn,if_exists= 'append',index = True)

#verificação
#método cursor() é utlizado para escrevermos as queries
cursor = conn.cursor()

query = '''
SELECT num_inscricao
FROM ENEM_2021
LIMIT 2;'''

print(cursor.execute(query).fetchall())

#fechando a conexão com o database
conn.close()
