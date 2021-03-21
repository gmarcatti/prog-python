#!/usr/bin/env python
# coding: utf-8

# # Localização - Alocação: O Problema de maximizar a cobertura

# Autor: Gustavo Eduardo Marcatti  
# 20 de março de 2021

# Bibliotecas necessárias

# In[1]:


import pandas as pd # Manipulação de dados
import geopandas as gpd # Manipulação de dados espaciais


# ## 1. Importar dados

# Arquivos das feições espaciais, disponibilizadas nos links a seguir, no formato geojson (modelo de transmissão de dados espaciais no formato texto, derivado do formato geral json, muito popular na internet).

# In[2]:


arq_antenas = "https://raw.githubusercontent.com/gmarcatti/prog-python/main/dados/antenas.geojson"
arq_infra = "https://raw.githubusercontent.com/gmarcatti/prog-python/main/dados/infraestrutura.geojson"


# Importar as feições espaciais e definir os campos `cod_antena` e `Cod_proj` como índices das respectivas tabelas

# In[3]:


antenas = gpd.read_file(arq_antenas)
antenas = antenas.set_index('cod_antena')
infra = gpd.read_file(arq_infra)
infra = infra.set_index('Cod_proj')


# ## 2. Pre-processamento

# Computar matriz de distâncias: matriz com i linhas (pontos de infraestruturas) e j colunas (antenas)

# In[4]:


dist_matriz = infra.geometry.apply(lambda g: antenas.distance(g))


# Considerar apenas os pontos da matriz em que a distância é menor do que o alcance da respectiva antena

# In[5]:


cond_dist = dist_matriz < antenas['alcance_m']
dist_alcance = dist_matriz[cond_dist]


# Converter a matriz formato padrão com i pontos de estruturas e j antenas (i *x* j) em uma matriz com i * j linhas e 3 colunas (pontos de estrutura, antenas e distâncias).

# In[6]:


dist_alcance = dist_alcance.stack().reset_index()


# Contabilização dos pontos de infraestruturas alcançados por cada uma das 9 antenas 

# In[7]:


dist_alcance.groupby('cod_antena')[0].count()


# ## 3. Solução aproximada com herística

# Preparação dos dados para execução do algoritmo. Dicionário (dict) em que a chave (key) é o código das antenas e os valores (value) é um conjunto (set) com os pontos de infraestruturas alcançados por cada uma das antenas

# In[8]:


antena_uni = dist_alcance['cod_antena'].unique()
antena_infra = {}
for ant in antena_uni:
    infra_i = set(dist_alcance[dist_alcance['cod_antena'] == ant]['Cod_proj'])
    antena_infra[ant] = infra_i


# Procedimento de maximização da cobertura propriamente dito

# In[9]:


n_antena = 9 # quantidade de antenas a serem selecionadas
infra_nao_coberto = set(dist_alcance['Cod_proj'])
antena_final = set()
while infra_nao_coberto:
    melhor_antena = None
    infra_coberta = set()
    for ant, inf in antena_infra.items():
        cobertos = infra_nao_coberto & inf
        if len(cobertos) > len(infra_coberta):
            melhor_antena = ant
            infra_coberta = cobertos  
    infra_nao_coberto -= infra_coberta
    antena_final.add(melhor_antena)
    print("Antena:", melhor_antena, "; Contribuição:", len(infra_coberta))
    if len(antena_final) >= n_antena: break


# ## 4. Solução ótima com Programação Inteira

# Bibliotecas necessárias

# In[10]:


import pulp


# ### 4.1 Preparar origem-destino e oferta-demanda

# Lista com códigos de Origens (infraestruturas) e Destinos (antenas)

# In[11]:


origem = list(set(dist_alcance['Cod_proj']))
destino = list(set(dist_alcance['cod_antena']))


# Oferta nas origens. Cada origem (infraestrutura) corresponde à uma unidade. Obs: Poderiamos utilizar a quantidade de madeira em m³ ofertadas em cada unidade e maximizar a quantidade de madeira coberta pelas antenas de comunicação

# In[12]:


oferta = {}
for i in range(len(dist_alcance)):
    oferta[ dist_alcance.at[i, 'Cod_proj'] ] = 1


# Demanda nos destinos. Cada destino (antena) é capaz de acessar uma demanda máxima (quantidade de infraestruturas) definidas pelo alcance da antena.

# In[13]:


demanda_max = dist_alcance.groupby('cod_antena').count()
demanda = {}
for i in demanda_max.index:
    demanda[i] = demanda_max.at[i, 'Cod_proj'] 


# ### 4.2 Modelo de programação inteira

# Maximização da cobertura de infraestruturas pelas antenas.  
#  
# $Max: FO = \sum \limits _{i=1} ^{o} \sum \limits _{j=1} ^{d} y _{ij} + \sum \limits _{j=1} ^{d} x _{j} \qquad origem \;(i..o): infraestrutura, \; destino \; (j..d): antena$
# <br>
# $ Sujeito \; a: $
# <br>
# $\sum \limits _{i=1} ^{o} \sum \limits _{j=1} ^{d} y _{ij} \leq D _{j} * x _{j} \qquad Demanda \; (j..D): antena$
# <br>
# $\sum \limits _{i=1} ^{o} \sum \limits _{j=1} ^{d} y _{ij} \leq O _{i} \qquad Oferta \; (i..O): infraestrutura$
# <br>
# $\sum \limits _{j=1} ^{d} x _{j} = Q \qquad destino \; (j..d): antena, \; Q: quantidade \;de \;antenas \;selecionadas$

# ### 4.3 Definir as variáveis do modelo

# Variável y: determina origem (infraestrutura) para destino (antena)

# In[14]:


y = {}
for i in range(len(dist_alcance)):
    o = dist_alcance.at[i, 'Cod_proj'] 
    d = dist_alcance.at[i, 'cod_antena'] 
    y[o, d] = pulp.LpVariable("y_%s_PARA_%s" % (o, d), 0, 1, pulp.LpBinary)


# Variável x: relacionada com as antenas, será útil para especificar a quantidade de antenas máximas

# In[15]:


x = {}
for i in destino:
    x[i] = pulp.LpVariable("x_%s" % i, 0, 1, pulp.LpBinary)


# ### 4.4 Criar o modelo

# Inicializar um novo modelo 

# In[16]:


m = pulp.LpProblem('Problema_do_alcance', pulp.LpMaximize)


# Função objetivo

# In[17]:


obj_func = []
for i in range(len(dist_alcance)):
    o = dist_alcance.at[i, 'Cod_proj'] 
    d = dist_alcance.at[i, 'cod_antena'] 
    obj_func.append( 1 * y[o, d] )


for i in destino:
    obj_func.append(x[i])


m += pulp.lpSum( obj_func)


# Retrições de demandas

# In[18]:


for d in destino:
    d_list = []
    for o in origem:
        if (o, d) in y:
            d_list.append(y[o, d])
    m += pulp.lpSum( d_list ) <= demanda[d] * x[d], "RestD_%s"%d 


# Retrições de ofertas

# In[19]:


for o in origem:
    o_list = []
    for d in destino:
        if (o, d) in y:
            o_list.append(y[o, d])
    m += pulp.lpSum( o_list ) <= oferta[o], "RestO_%s"%o 

m += pulp.lpSum( x ) == 2, "RestAntenas" 


# ### 4.5 Resolver o problema

# Solver com cbc (Coin-or branch and cut) disponibilizado em pulp

# In[20]:


m.solve(pulp.PULP_CBC_CMD())
print("Status: " + pulp.LpStatus[m.status])
print("Otimo (máximo): " + str(pulp.value(m.objective))) 


# ### 4.6 Capturar resultados da solução do modelo

# In[21]:


resul_name = []
resul_value = []
for v in m.variables()[len(x):]:
    #if v.varValue >= 0.1:
    resul_name.append(v.name)
    resul_value.append(v.varValue)

oferta_x_demanda = []
for i, var in enumerate(resul_name): #[9:]
    o, d = var.replace('y_', '').split('_PARA_')
    oferta_x_demanda.append([o, d, resul_value[i]]) # [9:]


resul = pd.DataFrame(oferta_x_demanda, columns=['Cod_proj', 'cod_antena', 'Atribuicao'])


# ### 4.7 Imprimir resultados 

# In[22]:


resumo = resul.groupby(['cod_antena'])['Atribuicao'].sum()
print("Resumo:", resumo)
print("Cobertura total:", resumo.sum())

