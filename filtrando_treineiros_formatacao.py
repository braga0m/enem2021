####pacotes
import pandas as pd
import numpy as np

######################dados - ENEM 2021
cols = ['NU_INSCRICAO','NU_ANO','TP_FAIXA_ETARIA','TP_SEXO','TP_COR_RACA','IN_TREINEIRO',
        'TP_ANO_CONCLUIU','TP_ESCOLA','NO_MUNICIPIO_ESC','SG_UF_ESC','NU_NOTA_CN','NU_NOTA_CH',
        'NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']

dados = pd.read_csv('C:/Users/Matias/Documents/Projetos_e_Estudos/ENEM_2021/DADOS/MICRODADOS_ENEM_2021.csv',
                     usecols=cols,
                     encoding='latin-1', sep = ';')


dados.head(20)

dados.shape#3389832 linhas  e 15 colunas

dados.describe()#resume as informações quantitativas

################algumas operações de interesse

#removendo colunas
dados = dados.drop(['NU_ANO'],axis=1)
dados.columns

#alterando nome das colunas
mapa = {
    'NU_INSCRICAO':'num_inscricao',
    'TP_FAIXA_ETARIA':'faixa_etaria',
    'TP_SEXO':'sexo',
    'TP_COR_RACA':'raca_cor',
    'TP_ANO_CONCLUIU':'ano_conclusao',
    'TP_ESCOLA':'escola',
    'IN_TREINEIRO':'treineiro',
    'NO_MUNICIPIO_ESC':'municipio',
    'SG_UF_ESC':'uf',
    'NU_NOTA_CN':'nota_ciencia_natureza',
    'NU_NOTA_LC':'nota_ciencia_humana',
    'NU_NOTA_MT':'nota_matematica',
    'NU_NOTA_LC':'nota_linguagens',
    'NU_NOTA_REDACAO':'redacao'
}
dados = dados.rename(columns=mapa)

#mudando o nome das categorias
#sexo
print(dados['sexo'].unique())
dados['sexo'] = dados['sexo'].replace({'M':'Masculino','F':'Feminino'})

#faixa etária
print(dados['faixa_etaria'].unique())
categorias_idade = ['Menor de 17 anos','17 anos','18 anos','19 anos','20 anos','21 anos','22 anos','23 anos','24 anos','25 anos',
                    'Entre 26 e 30 anos','Entre 31 e 35 anos','Entre 36 e 40 anos','Entre 41 e 45 anos','Entre 46 e 50 anos',
                    'Entre 51 e 55 anos','Entre 56 e 60 anos','Entre 61 e 65 anos','Entre 66 e 70 anos','Maior de 70 anos']
mapa_idade = dict(zip([i + 1 for i in range(20)],categorias_idade))
dados['faixa_etaria'] = dados['faixa_etaria'].replace(mapa_idade)

#raça/cor
print(dados['raca_cor'].unique())
categorias_raca = ['Não declarado','Branca','Preta','Parda','Amarela','Indígena','Não dispõe da informação']
mapa_raca = dict(zip([i for i in range(7)],categorias_raca))
dados['raca_cor'] = dados['raca_cor'].replace(mapa_raca)

#escola
print(dados['escola'].unique())
categorias_escola = ['Não Respondeu','Pública','Privada']
mapa_escola = dict(zip([i + 1 for i in range(3)],categorias_escola))
dados['escola'] = dados['escola'].replace(mapa_escola)

#filter
dados = dados[dados["treineiro"] == 0]
dados.shape

#exportar
dados.to_csv('ENEM_2021_sem_treineiros.csv')