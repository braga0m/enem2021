####pacotes
import pandas as pd
import numpy as np

###dados
dados = pd.read_csv('C:/Users/Matias/Documents/Projetos_e_Estudos/ENEM_2021/ENEM_2021_sem_treineiros.csv',
                    encoding='latin-1', sep = ';')

dados = dados.drop(['treineiro','Unnamed: 0'],axis=1)#axis argumento especifica q é p dropar a coluna (axis = 1 ou 'columns')

####infos
dados.columns
dados.head(10)
dados.shape
dados.describe()

####tabelas e medidas

