# 
  <div>
  <h1 align="center"> Microdados do ENEM 2021 (Análise Descritiva) 📚✏️</h1>
</div>

<h3>➡Sobre </h3>
A proposta deste projeto foi limpar, organizar e formatar os microdados do Exame Nacional do Ensino Médio (ENEM) de 2021, para enfim realizar uma análise descritiva dos dadose, e obter assim alguns insights e visualizações sobre os candidatos que realizaram o exame.

<h3>➡Passo a passo </h3>  

1. Fazer o download dos microdados.  
2. Configurar o ambiente para utilizar os pacotes Pandas e Numpy, do Python.
3. Realizar as diversas funções dos pacotes mencionados acima para tratar e formatar os dados.
4. Produzir informações relevantes sobre os dados.
5. Transformar o arquivo csv para um formato _database_ (.db).

Os microdados do ENEM desde 1998 podem ser encontrados aqui: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

<h3>➡Resultados </h3> 

O ENEM 2021 contou com mais de 3.3 milhões de incritos, sendo que aproximadamente 2.95 milhões eram cantidatos que se beneficiariam de algum direito que o exame proporciona. O restante eram indivíduos que fizeram a prova somente com a intenção de treinar, os treineiros. Assim, para fins de análise, foram retirados do conjunto de dados os treineiros e os candidatos que se inscreveram, porém não compareceram em nenhum dos dois dias da realização do exame. Totalizando, dessa maneira, aproximadamente 1.99 milhões de pessoas.

O conjunto de dados do ENEM é uma base importantíssima para analisar o perfil dos candidatos, com uma série de variáveis socioeconômicas que permitem estudar esses candidatos por diversos ângulos. No entanto, algumas informações chave, como por exemplo município e Unidade Federativa apresentam um elevado número de observações faltantes. Dado o recorte mencionado, mais de 68% desses indivíduos não possuem a informação sobre seu município e Estado de origem. 

Mesmo com algumas variáveis com qualidade fora do esperado, é intessante estudar o perfil dos candidatos que realizaram a prova. Por exemplo, dos quase 1.99 mihões que fizeram o exame ao menos um dos dois dias, aproxidamente 61% se identificaram como do sexo feminino e 39% masculino, uma diferença bastante significativa. Essa informação vai de encontro com a notícia pública em 2021 pelo site Globo, que afirma "Mulheres têm mais acesso ao ensino superior". O ENEM é umas das principais formas de ingresso do ensino público superior via Sistema de Seleção Unificada (SISU), assim se dentre os concorrentes das vagas mais de 60% são mulheres, é completamente natural imaginar isso se reflita nas vagas das universidades públicas. 

(Link da notícia mencionada: https://valor.globo.com/brasil/noticia/2021/03/04/ibge-mulheres-tem-mais-acesso-ao-ensino-superior-mas-ainda-sao-minoria-em-areas-como-engenharia-e-ti.ghtml) 

<p align="center">
  <img src="https://github.com/braga0m/enem2021/blob/main/pie_sexo.png"/>
</p>


Para ter acesso ao tratamento dos dados e o restante da análise acesse o arquivo: https://github.com/braga0m/enem2021/blob/main/analises_medidas.ipynb














