#pacotes
import pandas as pd
import numpy as np

#importando dados
dados = pd.read_csv('C:/Users/Matias/Documents/Projetos_e_Estudos/ENEM_2021/DADOS/ENEM_2021_sem_treineiros.csv',
                    encoding='UTF-8', sep = ',')
dados.head(10)


#removendo colunas
#axis argumento especifica q é p dropar a coluna (axis = 1 ou 'columns')
dados = dados.drop(['treineiro','Unnamed: 0'],axis=1)

mapa = {'NU_NOTA_CH':'nota_ciencia_humana'}
dados = dados.rename(columns=mapa)


#checando os dados
dados.columns
dados.info()
dados.shape


#verificando valores únicos - duas opções
len(dados['num_inscricao'].unique())
(dados.num_inscricao.unique())

#checando missing values
sum(dados['escola'].isnull())
sum(dados['nota_matematica'].isnull())
sum(dados['nota_linguagens'].isnull())
sum(dados['redacao'].isnull())
sum(dados['nota_ciencia_natureza'].isnull())
sum(dados['nota_ciencia_humana'].isnull())


#número de missing values de todas as variáveis
num_na = np.array([sum(dados[i].isnull()) for i in list(dados.columns)])
prop_na = num_na/len(dados)

d = {'var':list(dados.columns), 'num_na':num_na, 'prop':prop_na.round(2)}
na_count = pd.DataFrame(data = d).sort_values(by=['num_na'], ascending = False)
print(na_count)


#selecionando colunas
dados['escola']
sum(dados['escola'] == 'Pública')
(dados['escola'] == 'Pública').sum()

dados[['escola','raca_cor']]


#substituindo missing values das notas das provas por zero
dados['nota_matematica'] = dados['nota_matematica'].fillna(0)
dados['nota_ciencia_humana'] = dados['nota_ciencia_humana'].fillna(0)
dados['redacao'] = dados['redacao'].fillna(0)
dados['nota_ciencia_natureza'] = dados['nota_ciencia_natureza'].fillna(0)
dados['nota_linguagens'] = dados['nota_linguagens'].fillna(0)

#substituindo missing values de uf e municipios por vazio
dados['uf'] = dados['uf'].fillna('')
dados['municipio'] = dados['municipio'].fillna('')


#eliminando candidatos que tiraram zero nas 5 áreas do conhecimento - ausentes - não foram fazer a prova
dados = dados.query('(nota_matematica + nota_ciencia_natureza + redacao + nota_linguagens + nota_ciencia_humana) != 0')


#criando a variável status de acordo com as notas - todas as notas maiores que zero
dados['status'] = np.where(((dados['nota_matematica'] == 0) | (dados['nota_ciencia_natureza'] == 0) | (dados['redacao'] == 0) | (dados['nota_linguagens'] == 0) | 
                           (dados['nota_ciencia_humana'] == 0)),'Não Habilitado','Habilitado')



#exportando em formato excel
dados.to_csv('ENEM_2021_FINAL.csv')