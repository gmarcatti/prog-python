# prog-python
Procedimentos apresentados na disciplina de Algoritmos e programação computacional no Python

# Semana 08 - Exercício: O Problema de maximizar a cobertura (Localização - Alocação)

Autor: Gustavo Eduardo Marcatti  
20 de março de 2021

Bibliotecas necessárias


```python
import pandas as pd # Manipulação de dados
import geopandas as gpd # Manipulação de dados espaciais
```

## 1. Importar dados

Arquivos das feições espaciais, disponibilizadas nos links a seguir, no formato geojson (modelo de transmissão de dados espaciais no formato texto, derivado do formato geral json, muito popular na internet).


```python
arq_antenas = "https://raw.githubusercontent.com/gmarcatti/prog-python/main/dados/antenas.geojson"
arq_infra = "https://raw.githubusercontent.com/gmarcatti/prog-python/main/dados/infraestrutura_projeto.geojson"
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



## 3. Solução aproximada

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
