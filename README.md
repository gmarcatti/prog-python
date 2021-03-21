# prog-python
Procedimentos apresentados na disciplina de Algoritmos e programação computacional no Python

[Semana 08 - Estruturas de dados no Python](#Semana-08---Estruturas-de-dados-no-Python)
- [Código aula](#Código-aula)
  - [Parte 1](#Parte-1)
- [Exercícios](#Exercícios)
  - [O Problema de maximizar a cobertura (Localização - Alocação)](#O-Problema-de-maximizar-a-cobertura-(Localização---Alocação))
    - [1. Importar dados](#1.-Importar-dados)
    - [2. Pre-processamento](#2.-Pre-processamento)
    - [3. Solução aproximada com herística](#3.-Solução-aproximada-com-herística)
    - [4. Solução ótima com Programação Inteira](#4.-Solução-ótima-com-Programação-Inteira)


# Semana 08 - Estruturas de dados no Python

# Código aula
## Parte 1

# Exercícios
## O Problema de maximizar a cobertura (Localização - Alocação)

Autor: Gustavo Eduardo Marcatti  
20 de março de 2021

Dentre as 9 possibilidades viáveis de alocação de antenas de comunicação, apenas as duas melhores deverão ser construidas. Quais são as duas melhores?  
Resposta: antenas que maximizam a cobertura de pontos de infraestrutura.
O objetivo do problema é `maximizar` a `cobertura` de pontos de `infraestrutura` de projetos florestais por uma quantidade fixa, previamente estabelecida, de `antenas` de comunicação. Algumas restrições devem ser estabelecidas: (1) cada antena apresenta uma quantidade máxima de acesso de pontos de infraestrutura, quantidade determinada pela distância infraestrutura-antena e alcance máximo da antena (m); (2) cada ponto de infraestrutura só deve ser acessado por uma única antena (o ponto deve estar dentro do raio máximo de alcance da antena selecionada); (3) A quantidade de antenas selecionadas deverá ser igual a quantidade previamente estabelecida (no presente estudo igual a duas).
![alt text](https://raw.githubusercontent.com/gmarcatti/prog-python/main/img/fig_geral.png)

Bibliotecas necessárias


```python
import pandas as pd # Manipulação de dados
import geopandas as gpd # Manipulação de dados espaciais
```

## 1. Importar dados

Arquivos das feições espaciais, disponibilizadas nos links a seguir, no formato geojson (modelo de transmissão de dados espaciais no formato texto, derivado do formato geral json, muito popular na internet).


```python
arq_antenas = "https://raw.githubusercontent.com/gmarcatti/prog-python/main/dados/antenas.geojson"
arq_infra = "https://raw.githubusercontent.com/gmarcatti/prog-python/main/dados/infraestrutura.geojson"
```

Importar as feições espaciais e definir os campos `cod_antena` e `Cod_proj` como índices das respectivas tabelas


```python
antenas = gpd.read_file(arq_antenas)
antenas = antenas.set_index('cod_antena')
infra = gpd.read_file(arq_infra)
infra = infra.set_index('Cod_proj')
```

## 2. Pre-processamento

Computar matriz de distâncias: matriz com i linhas (pontos de infraestruturas) e j colunas (antenas)


```python
dist_matriz = infra.geometry.apply(lambda g: antenas.distance(g))
```
    

Considerar apenas os pontos da matriz em que a distância é menor do que o alcance da respectiva antena


```python
cond_dist = dist_matriz < antenas['alcance_m']
dist_alcance = dist_matriz[cond_dist]
```

Converter a matriz formato padrão com i pontos de estruturas e j antenas (i *x* j) em uma matriz com i * j linhas e 3 colunas (pontos de estrutura, antenas e distâncias).


```python
dist_alcance = dist_alcance.stack().reset_index()
```

Contabilização dos pontos de infraestruturas alcançados por cada uma das 9 antenas 


```python
dist_alcance.groupby('cod_antena')[0].count()
```




    cod_antena
    a1    44
    a2     9
    a3    32
    a4    37
    a5    25
    a6    22
    a7    10
    a8     4
    a9    40
    Name: 0, dtype: int64



## 3. Solução aproximada com herística

Preparação dos dados para execução do algoritmo. Dicionário (dict) em que a chave (key) é o código das antenas e os valores (value) é um conjunto (set) com os pontos de infraestruturas alcançados por cada uma das antenas


```python
antena_uni = dist_alcance['cod_antena'].unique()
antena_infra = {}
for ant in antena_uni:
    infra_i = set(dist_alcance[dist_alcance['cod_antena'] == ant]['Cod_proj'])
    antena_infra[ant] = infra_i
```

Procedimento de maximização da cobertura propriamente dito


```python
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
```

    Antena: a1 ; Contribuição: 44
    Antena: a3 ; Contribuição: 32
    Antena: a4 ; Contribuição: 27
    Antena: a6 ; Contribuição: 12
    Antena: a5 ; Contribuição: 3
    Antena: a2 ; Contribuição: 2
    Antena: a7 ; Contribuição: 2
    Antena: a9 ; Contribuição: 1
    Antena: a8 ; Contribuição: 1
    

## 4. Solução ótima com Programação Inteira

Bibliotecas necessárias


```python
import pulp
```

    Academic license - for non-commercial use only - expires 2021-05-06
    Using license file C:\Users\Adm\gurobi.lic
    No parameters matching '_test' found
    

### 4.1 Preparar origem-destino e oferta-demanda

Lista com códigos de Origens (infraestruturas) e Destinos (antenas)


```python
origem = list(set(dist_alcance['Cod_proj']))
destino = list(set(dist_alcance['cod_antena']))
```

Oferta nas origens. Cada origem (infraestrutura) corresponde à uma unidade. Obs: Poderiamos utilizar a quantidade de madeira em m³ ofertadas em cada unidade e maximizar a quantidade de madeira coberta pelas antenas de comunicação


```python
oferta = {}
for i in range(len(dist_alcance)):
    oferta[ dist_alcance.at[i, 'Cod_proj'] ] = 1
```

Demanda nos destinos. Cada destino (antena) é capaz de acessar uma demanda máxima (quantidade de infraestruturas) definidas pelo alcance da antena.


```python
demanda_max = dist_alcance.groupby('cod_antena').count()
demanda = {}
for i in demanda_max.index:
    demanda[i] = demanda_max.at[i, 'Cod_proj'] 
```

### 4.2 Modelo de programação inteira

Maximização da cobertura de infraestruturas pelas antenas.  

![alt text](https://raw.githubusercontent.com/gmarcatti/prog-python/main/img/modelo_equacao.PNG)

### 4.3 Definir as variáveis do modelo

Variável y: determina origem (infraestrutura) para destino (antena)


```python
y = {}
for i in range(len(dist_alcance)):
    o = dist_alcance.at[i, 'Cod_proj'] 
    d = dist_alcance.at[i, 'cod_antena'] 
    y[o, d] = pulp.LpVariable("y_%s_PARA_%s" % (o, d), 0, 1, pulp.LpBinary)
```

Variável x: relacionada com as antenas, será útil para especificar a quantidade de antenas máximas


```python
x = {}
for i in destino:
    x[i] = pulp.LpVariable("x_%s" % i, 0, 1, pulp.LpBinary)
```

### 4.4 Criar o modelo

Inicializar um novo modelo 


```python
m = pulp.LpProblem('Problema_do_alcance', pulp.LpMaximize)
```

Função objetivo


```python
obj_func = []
for i in range(len(dist_alcance)):
    o = dist_alcance.at[i, 'Cod_proj'] 
    d = dist_alcance.at[i, 'cod_antena'] 
    obj_func.append( 1 * y[o, d] )


for i in destino:
    obj_func.append(x[i])


m += pulp.lpSum( obj_func)
```

Retrições de demandas


```python
for d in destino:
    d_list = []
    for o in origem:
        if (o, d) in y:
            d_list.append(y[o, d])
    m += pulp.lpSum( d_list ) <= demanda[d] * x[d], "RestD_%s"%d 
```

Retrições de ofertas


```python
for o in origem:
    o_list = []
    for d in destino:
        if (o, d) in y:
            o_list.append(y[o, d])
    m += pulp.lpSum( o_list ) <= oferta[o], "RestO_%s"%o 

m += pulp.lpSum( x ) == 2, "RestAntenas" 
```

### 4.5 Resolver o problema

Solver com cbc (Coin-or branch and cut) disponibilizado em pulp


```python
m.solve(pulp.PULP_CBC_CMD())
print("Status: " + pulp.LpStatus[m.status])
print("Otimo (máximo): " + str(pulp.value(m.objective))) 
```

    Status: Optimal
    Otimo (máximo): 78.0
    

### 4.6 Capturar resultados da solução do modelo


```python
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
```

### 4.7 Imprimir resultados 


```python
resumo = resul.groupby(['cod_antena'])['Atribuicao'].sum()
print("Resumo:", resumo)
print("Cobertura total:", resumo.sum())
```

    Resumo: cod_antena
    a1    44.0
    a2     0.0
    a3    32.0
    a4     0.0
    a5     0.0
    a6     0.0
    a7     0.0
    a8     0.0
    a9     0.0
    Name: Atribuicao, dtype: float64
    Cobertura total: 76.0
    
