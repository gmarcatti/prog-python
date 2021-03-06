# prog-python
Procedimentos apresentados na disciplina de Algoritmos e programação computacional no Python

# Índice

[Semana 02 - Variáveis e Funções no Python](#Semana-02---Variáveis-e-Funções-no-Python)


[Semana 03 - Condicionais no Python - Operadores e Sinais](#Semana-03---Condicionais-no-Python---Operadores-e-Sinais)


[Semana 04 - Condicionais no Python - Lógicas e Aninhamento](#Semana-04---Condicionais-no-Python---Lógicas-e-Aninhamento)

[Semana 08 - Estruturas de dados no Python](#Semana-08---Estruturas-de-dados-no-Python)

[Semana 10 - Programação Funcional no Python](#Semana-10---Programação-Funcional-no-Python)

---


<!-- ------------------------------------------------------------ -->
<!-- Semana 02 - Variáveis e Funções no Python  -->
<!-- ------------------------------------------------------------ -->



# Semana 02 - Variáveis e Funções no Python

[:arrow_left:](#Índice) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_up:](#Índice) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_right:](#Semana-03---Condicionais-no-Python---Operadores-e-Sinais)

**Neste tópico você irá aprender a executar operações matemáticas básicas, criar variáveis, executar e criar suas próprias funções.**

O tempo todo no Python é necessário criar novas variáveis, elas serão úteis para armazenar resultados intermediários e até mesmo resultados finais.

Uma das maiores potencialidades do Python é que ele permite ao usuário definir suas próprias funções de forma simples e fácil. Isso o torna uma ferramenta poderosa para criar e testar novas metodologias. No Python as funções apresentam papel de destaque, pois é uma das principais formas de interagir com as rotinas nativas da linguagem.


[Código aula](#Código-aula-02)
- [1. Operações básicas](#1-Operações-básicas)
- [2. Imprimir na tela](#2-Imprimir-na-tela)
- [3. Executar funções](#3-Executar-funções)
- [4. Criar variáveis](#4-Criar-variáveis)
- [5. Criar funções](#5-Criar-funções)


[Exercícios](#Exercícios-02)


# Código aula 02

## 1. Operações básicas

```python
a = 2
b = 3
a + b
a * b
```

## 2. Imprimir na tela

```python
a + b
print(a + b)

print("Seja bem vindo!")
```

## 3. Executar funções

```python
import math
math.log(2)
math.log(2, 3)
math.log(2)
math.log(2, math.e)
# math.log(, math.e) # erro
```

## 4. Criar variáveis

```python
log_valor = math.log(2)
resultado_final = log_valor * 45.1
resultado_final
print(resultado_final)

obj1 = math.sqrt(25)
obj2 = math.sqrt(12)

nome = "Eduardo"
```


## 5. Criar funções

## Exemplo de boas vindas

> 1 - Sem argumentos e sem retorno
```python
def boas_vindas1():
    print("Seja bem vindo!")

boas_vindas1()
```

> 2 - Com argumento
```python
def boas_vindas2(nome):
    print("Seja bem vindo", nome, "!")

boas_vindas2("Fulano")
```
> 3 - Com argumento padrão
```python
def boas_vindas3(nome = "aluno"):
    print("Seja bem vindo", nome, "!")

boas_vindas3()
boas_vindas3("Fulano")
```

## Exemplo análise econômica de projetos 

> 4 - Com retorno

> Com repetição de código. Indesejável, pois é necessário muito código repetido

```python
# Proj1
receita = 6000
custo = 4000
lucro = receita - custo
print(lucro)

# Proj2
receita = 9000
custo = 5000
lucro = receita - custo
print(lucro)

# Proj3
receita = 6000
custo = 6500
lucro = receita - custo
print(lucro)
```

> Com função! Ideal, pois evita códigos repetidos e assim facilita o ato de programar, revisar e manter o código, além de minimizar as possibilidades de erro
```python
def aval_eco(receita, custo):
    lucro = receita - custo
    return(lucro)
    
proj1 = aval_eco(6000, 4000)
proj2 = aval_eco(9000, 5000)
proj3 = aval_eco(6000, 6500)

lucro_geral = proj1 + proj2 + proj3
lucro_geral
```

Bloco de execução inicializado com ` : ` e encerrado com o fim da indentação

```python
def funcao():
    a = 3
    b = 3
    cv = a * b
    return(cv)

funcao()
```

# Exercícios 02

---


<!-- ------------------------------------------------------------ -->
<!-- Semana 03 - Condicionais no Python: Operadores e Sinais  -->
<!-- ------------------------------------------------------------ -->

# Semana 03 - Condicionais no Python - Operadores e Sinais

[:arrow_left:](#Semana-02---Variáveis-e-Funções-no-Python) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_up:](#Índice) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_right:](#Semana-04---Condicionais-no-Python---Lógicas-e-Aninhamento)

**Você irá aprender sobre os operadores condicionais e operadores de comparação. O primeiro corresponde à estrutura geral das operações de condição (Ex: if...else), já o segundo trata dos sinais utilizados para construir as operações de condição (Ex: > maior que, != diferente).**

`As operações condicionais estão relacionadas com tomada de decisão entre diferentes alternativas, isto é, escolha de uma opção entre duas ou mais possibilidades.` Para ser capaz de compreender as operações condicionais é necessário estudar pelo menos 4 temas: os operadores `condicionais`, operadores de `comparação`, operadores `lógicos` e operadores `condicionais aninhados`. Os dois primeiros serão apresentados no tópico atual e os dois últimos no tópico seguinte.


[Código aula](#Código-aula-03)
- [Exemplo 1 - Avaliação econômica](#Exemplo-1---Avaliação-econômica)
  - [1. Condicional if](#1-Condicional-if)
  - [2. Condicional if-else](#2-Condicional-if-else)
  - [3. Condicional if-elif-else](#3-Condicional-if-elif-else)
- [Exemplo 2 - Decisão de expansão de área](#Exemplo-2---Decisão-de-expansão-de-área)


[Exercícios](#Exercícios-03)

# Código aula 03

## Exemplo 1 - Avaliação econômica
Identificar se o projeto retorna lucro, prejuízo ou nenhum dos dois, utilizando as informações de receitas e custos do projeto. 

### 1. Condicional if
```python
receita = 7000
custo = 8000
resultado = receita - custo
if resultado > 0:
    print("Projeto com lucro!")
```

### 2. Condicional if-else
```python
receita = 8000
custo = 8000
resultado = receita - custo
if resultado > 0:
    print("Projeto com lucro de R$", resultado)
else:
    print("Projeto com prejuízo de R$", abs(resultado))
```

### 3. Condicional if-elif-else
```python
receita = 7000
custo = 9000
resultado = receita - custo
if resultado > 0:
    print("Projeto com Lucro de R$", resultado)
elif resultado == 0:
    print("Projeto sem lucro... e sem prejuízo")
else:
    print("Projeto com Prejuízo de R$", abs(resultado))
```

> 1 - Criar função
```python
def aval_eco(receitas, custos):
    resultado = receitas - custos
    if resultado > 0:
        print("Projeto com Lucro de R$", resultado)
    elif resultado == 0:
        print("Projeto sem lucro... e sem prejuízo")
    else:
        print("Projeto com Prejuízo de R$", abs(resultado))
    return(resultado)
```

> 2 - Aplicar a função
```python
proj1 = aval_eco(9000, 5000)
proj2 = aval_eco(5000, 5000)
proj3 = aval_eco(4500, 5000)

print("Total R$", proj1 + proj2 +proj3)
```


## Exemplo 2 - Decisão de expansão de área
Decidir qual deve ser a área de expansão de plantio de determinada cultura agrícola para o ano seguinte. A quantidade de expansão varia de acordo com o sucesso do ano atual. O sucesso é medido por uma proporção entre receita e custo da safra atual. As opções são: 0, 20, 50 e 100% de expansão.
```python
receita = 14000
custo = 6000

prop = receita / custo
area2021 = 200
if prop <= 1:
    area2022 = area2021
    print("Área de plantio em 2022 (0%):", area2022)
elif prop <= 1.5:
    area2022 = area2021 * 1.2
    print("Área de plantio em 2022 (20%):", area2022)
elif prop <= 2:
    area2022 = area2021 * 1.5
    print("Área de plantio em 2022 (50%):", area2022)
else:
    area2022 = area2021 * 2
    print("Área de plantio em 2022 (100%):", area2022)
```

> 1 - Criar função
```python
def exp_area(receitas, custos, area_atual):
    prop = receitas / custos
    area_atual = 200
    if prop <= 1:
        area_prox = area_atual
        print("Área de plantio em 2022 (0%):", area_prox)
    elif prop <= 1.5:
        area_prox = area_atual * 1.2
        print("Área de plantio em 2022 (20%):", area_prox)
    elif prop <= 2:
        area_prox = area_atual * 1.5
        print("Área de plantio em 2022 (50%):", area_prox)
    else:
        area_prox = area_atual * 2
        print("Área de plantio em 2022 (100%):", area_prox)
    return(area_prox)
```

> 2 - Aplicar a função
```python
exp_area(4000, 5000, 200)
exp_area(6000, 5000, 200)
exp_area(9000, 5000, 200)
exp_area(11000, 5000, 200)
```

# Exercícios 03

---

<!-- ------------------------------------------------------------ -->
<!-- Semana 04 - Operações Condicionais - Lógicas e Aninhamento  -->
<!-- ------------------------------------------------------------ -->
# Semana 04 - Condicionais no Python - Lógicas e Aninhamento

[:arrow_left:](#Semana-03---Condicionais-no-Python---Operadores-e-Sinais) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_up:](#Índice) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_right:](#Semana-08---Estruturas-de-dados-no-Python)


**Você irá aprender sobre os operadores lógicos, os representantes principais são o `ou` e `e`, representados pelas palavras reservadas `or` e `and`, ou então pelos símbolos `|` e `&`, respectivamente. Você também será apresentado aos condicionais aninhados, que podem ser utilizados para substituir um operador lógico. Um condicional aninhado, é basicamente, um operador condicional dentro do outro.**

O operador `and` pode ser considerado mais restritivo, uma vez que só retorna verdadeiro se todas as expressões de condição forem verdadeiras. Já o operador `or` é considerado mais permissivo, pois basta uma expressão ser verdadeira para toda a condição retornar verdadeiro no final. A escolha do operador lógico, obviamente vai depender do problema em questão.

Os operadores lógicos podem ser substituídos por operadores condicionais aninhados (ou encaixados). As vezes vale a pena recorrer a essas estruturas de condição por questões de simplificação. Com os condicionais aninhados o código pode ficar mais simples de implementar e entender.


[Código aula](#Código-aula-03)
- [Exemplo 1 - Área prioritária](#Exemplo-1---Área-prioritária)
  - [1. Solução simplificada](#1-Solução-simplificada)
  - [2. Solução completa](#2-Solução-completa)
- [Exemplo 2 - Condicional aninhado](#Exemplo-2---Condicional-aninhado)

# Exemplo 1 - Área prioritária

Determinar se a área é prioritária para recuperação ambiental, de acordo com os critérios a seguir:
>1: área de solo exposto acima 5% do total
>
>2: área contínua de solo exposto acima 5 ha

Importar as bibliotecas necessárias
```python
from osgeo import gdal # importar raster
import numpy as np # operações com dados no formato matricial
from scipy.ndimage import label # identificar grupos isolados
import matplotlib.pyplot as plt # plotar dados
```
## 1. Solução simplificada
Solução em que as medidas de porcentagem de solo exposto `solo_porc` e quantidade de área contínua de solo exposto `solo_cont` são fornecidas
```python
solo_porc = 10 # porcentagem
solo_cont = 3 # hectares
```

Condicional com o operador lógico or (ou) para determinar se a área deve ser considerada prioritária ou não
```python
if solo_porc > 5 or solo_cont > 5:
    print("********* Prioritária *********")
else:
    print("--- Não prioritária ---")
```

## 2. Solução completa
Na solução completa as medidas de porcentagem de solo exposto `solo_porc` e quantidade de área contínua de solo exposto `solo_cont` são obtidas de forma automática utilizando operações matriciais básicas  
<br/>
Os dados podem ser acessados aqui https://gmarcatti.github.io/dados/uso_terra.tif
<br/>
> 1 - Importar o raster com os dados de uso e ocupação da terra
```python  
uso_terra = r"C:\dados\espacial\uso_terra.tif"
```
Obs: alterar o caminho acima de acordo com o caminho dos dados em seu computador após o download

```python  
uso_raster = gdal.Open(uso_terra)
banda = uso_raster.GetRasterBand(1)
uso_matriz = banda.ReadAsArray()

uso_matriz[uso_matriz <= 0] = 0 # atribuir 0 nos valores nodata
plt.imshow(uso_matriz) # plotar os dados
```
> 2 - Área de solo exposto acima 5% do total

```python 
v_uso, cont_uso = np.unique(uso_matriz, return_counts = True)
cont_uso = cont_uso[1:]
porc_uso = 100 * cont_uso / cont_uso.sum()
porc_solo = porc_uso[2]
```
> 3 - Área contínua de solo exposto acima 5 ha
```python 
solo_matriz = uso_matriz == 3
plt.imshow(solo_matriz)

solo_label, num_label = label(solo_matriz)
plt.imshow(solo_label)

v_solo, cont_solo = np.unique(solo_label, return_counts = True)
cont_solo = cont_solo[1:]
area_pixel = 40 * 40

solo_cont = cont_solo * area_pixel / 10000
solo_cont_max = solo_cont.max()
```

> 4 - Decisão
```python 
if porc_solo > 5 or solo_cont_max > 5:
    print("***** Prioritária ******")
else:
    print("--- Não prioritária ---")
```

# Exemplo 2 - Condicional aninhado

Definir ação controle de acordo com nível de infestação de uma praga. As opções básicas são continuar com o programa atual, intensificar a amostragem, agir para controlar e não adianta fazer mais nada. Dentro da alternativa de intensificar temos 3 opções possíveis: repetir a amostragem a cada 4 dias, 2 dias e todos os dias

> 1 - Criar função

```python 
def controle(nivel):
    if nivel <= 2:
        print("Não mudar nada no programa atual")
    elif nivel > 2 and nivel <= 4:
        print("Intensificar a amostragem")
        if nivel > 2 and nivel <= 3:
            print("Repetir de 4 em 4 dias")
        elif nivel > 3 and nivel <= 3.5:
            print("Repetir de 2 em 2 dias")
        elif nivel > 3.5 and nivel < 4:
            print("Repetir todos os dias")
    elif nivel > 4 and nivel <= 20:
        print("AÇÃO: tentar controlar")
    else:
        print("Não adianta fazer mais nada...")
```

> 2 - Aplicar a função
```python 
controle(1.5)
controle(2.5)
controle(3.1)
controle(3.9)
controle(5.2)
controle(22.7)
```

> 3 - Aplicar a função em um loop
```python 
niveis = [1.5, 2.5, 3.1, 3.9, 5.2, 22.7]
for nivel in niveis:
    print("------------------")
    print("Para o nivel:", nivel)
    controle(nivel)
```
Obs: Os processos de repetição em loop serão ensinados no próximo tema

---

<!-- ------------------------------------------------------------ -->
<!-- Semana 08 - Estruturas de dados no Python  -->
<!-- ------------------------------------------------------------ -->

# Semana 08 - Estruturas de dados no Python

[:arrow_left:](#Semana-04---Condicionais-no-Python---Lógicas-e-Aninhamento) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_up:](#Índice) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_right:](#Semana-10---Programação-Funcional-no-Python)


[Código aula](#Código-aula-08)
- [Parte 1](#Parte-1)

[Exercícios](#Exercícios-08)
- [O Problema de maximizar a cobertura (Localização - Alocação)](#O-Problema-de-maximizar-a-cobertura-Localização---Alocação)
  - [1. Importar dados](#1-Importar-dados)
  - [2. Pre-processamento](#2-Pre-processamento)
  - [3. Solução aproximada com herística](#3-Solução-aproximada-com-herística)
  - [4. Solução ótima com Programação Inteira](#4-Solução-ótima-com-Programação-Inteira)

# Código aula 08
## Parte 1

# Exercícios 08
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

Função Objetivo (FO): Maximização da cobertura de infraestruturas pelas antenas, sujeito às restrições: (1) cada antena apresenta uma quantidade máxima de acesso de pontos de infraestrutura (restrições de demanda); (2) cada ponto de infraestrutura só deve ser acessado por uma única antena (restrições de ofertas); (3) A quantidade de antenas selecionadas deverá ser igual a quantidade previamente estabelecida (igual a 2 neste caso).  

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

Variável x: relacionada com as antenas, será útil para especificar a quantidade de antenas desejadas


```python
x = {}
for i in destino:
    x[i] = pulp.LpVariable("x_%s" % i, 0, 1, pulp.LpBinary)
```

### 4.4 Criar o modelo

Inicializar um novo modelo de maximização utilizando a biblioteca pulp (para gerar modelos de programação linear, inteira e mista) do Python


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

Restrições de demandas


```python
for d in destino:
    d_list = []
    for o in origem:
        if (o, d) in y:
            d_list.append(y[o, d])
    m += pulp.lpSum( d_list ) <= demanda[d] * x[d], "RestD_%s"%d 
```

Restrições de ofertas


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
print("Ótimo (máximo): " + str(pulp.value(m.objective))) 
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

### 4.7 Imprimir resultados na tela


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
    

# Semana 10 - Programação Funcional no Python

[:arrow_left:](#Semana-08---Estruturas-de-dados-no-Python) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_up:](#Índice) &nbsp; &nbsp; &nbsp; &nbsp; [:arrow_right:](#Índice)


[Código aula](#Código-aula-10)


[Exercícios](#Exercício-10)


[Exercício Extra](#Exercício-extra-10)
- [Ajuste de regressão para grupos de dados](#Ajuste-de-regressão-para-grupos-de-dados)
  - [Apresentação dos dados](#Apresentação-dos-dados)
  - [1. Paradigma Imperativo](#1-Paradigma-Imperativo)
  - [2. Paradigma Funcional](#2-Paradigma-Funcional)
  - [3. Paradigma Vetorizado](#3-Paradigma-Vetorizado)

# Código aula 10


## Exercício 10

# Exercício extra 10
## Ajuste de regressão para grupos de dados

Autor: Gustavo Eduardo Marcatti  
03 de abril de 2021

O exercício apresenta a solução para o ajuste de modelos de regressão linear para grupos de elementos, estes grupos estão reunidos em uma base de dados. Os grupos correspondem a estratos dos dados que compartilham de características semelhantes, como material genético, região, manejo, dentre outras. Os procedimentos desenvolvidos servem para ajustar um modelo de regressão linear simples (y = b0 + b1 * x), porém pode ser adaptado para o ajuste de outros modelos de regressão linear e até mesmo de regressão não linear. Três paradigmas de programação diferentes foram utilizadas para os ajustes: (1) Imperativo, (2) Funcional e (3) Vetorizado.

Bibliotecas necessárias para o processamento

```python
import pandas as pd # Análises em data frame (quadro de dados)
import numpy as np # Análises em array (matrizes)
from scipy.sparse import hstack, csc_matrix, linalg # Análises em matrizes esparsas
```

## Apresentação dos dados
```python
proj = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3] # código do projeto (grupo)
x =    [1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4] # variável x
y =    [1, 2, 2, 3, 8, 6, 5, 3, 2, 4, 5, 8, 9] # Variável y
lista = zip(proj, x, y) # juntar as três listas de dados em uma lista única
col = ['proj', 'x', 'y'] # nome das colunas da data frame
dados = pd.DataFrame(lista, columns = col) # criar data frame com os dados
dados # imprimir os dados na tela
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>proj</th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>1</td>
      <td>8</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>11</th>
      <td>3</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3</td>
      <td>4</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>


## 1. Paradigma Imperativo
O paradigma imperativo utiliza processo de repetição explícita com a estrutura de controle loop for. Os passos elementares são descritos a seguir:
> 1 - Ordenar dados pelos grupos (proj) de interesse  
> 2 - Criar lista vazia para receber os valores dos parâmetros (ou coeficiêntes) do modelo  
> 3 - Definir o loop for para controlar as repetições para cada projeto (grupo). Os grupos são gerados pela aplicação da função [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) da biblioteca [itertools](https://docs.python.org/3/library/itertools.html) a partir da combinação dos dados de colunas em linhas pela função `zip`
> 4 - Obter cada coluna de interesse dos dados para o grupo `k`, a partir da aplicação do inverso da função `zip`
> 5 - Criar matriz a `X` <sub>`n x m`</sub> em que `n` é o número de observações do grupo `k` e `m` é o número de coeficiêntes do modelo, neste caso a matriz `X` apresenta 2 colunas: variável explicativa `x` e coluna com valor constante, igual a 1, de modo que o primeiro corresponde ao coeficiente angular (b1) e o segundo ao coeficiente linear (b0).  
> 6 - Ajustar o modelo `y = b0 + b1 * x`, utilizando a função [lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html), de ajuste via minimos quadrados (least-squares) da biblioteca numpy.  
> 7 - Armazenar os coeficientes do modelo, correspondente ao grupo `k`, na lista criada em (2).  
> 8 - Salvar os coeficientes em uma data frame do pandas

```python
from itertools import groupby
from operator import itemgetter
d.sort_values('proj', inplace = True) # ordenar por grupos
coef = []
for k, g in groupby(zip(d['proj'], d['x'], d['y']), key=itemgetter(0)):
    proj, x, y = zip(*g)
    X = np.vstack([x, np.ones(len(y))]).T
    b1, b0 = np.linalg.lstsq(X, y, rcond=None)[0]
    coef.append([k, b0, b1])
col = ['proj', 'b0', 'b1']
coef_imp = pd.DataFrame(coef, columns = col)
coef_imp
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>proj</th>
      <th>b0</th>
      <th>b1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.5</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>9.3</td>
      <td>-1.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>
</div>

<br>   


Vale apena pesquisar mais sobre a função [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) da biblioteca [itertools](https://docs.python.org/3/library/itertools.html), essa biblioteca já vêm com a instalação padrão do Python, e apresenta uma série de outras funções que podem ser extremamente úteis para automatizar tarefas.

<br>
<br>


## 2. Paradigma Funcional

O paradigma funcional utiliza processo de repetição implícita com a aplicação do método group_by seguido do apply, assim uma função previamente definida, para ajustar o modelo é aplicada repetidamente para cada grupo da base de dados. Esse procedimento pode ser conhecido como group-by ou split-apply-combine. Os passos elementares são descritos a seguir:

> 1 - Criar função para o ajuste  
> 1.1 - Isolar a coluna referente à variável resposta `y`  
> 1.2 - Criar matriz a `X` <sub>`n x m`</sub> assim como descrito no paradigma imperativo  
> 1.3 -  Ajustar o modelo `y = b0 + b1 * x`, utilizando a função [lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html), como no paradigma imperativo  
> 1.4 - Salvar os coeficientes (`b0` e `b1`) em uma data frame  
> 2 - Em uma única linha de comando: subdividir os dados em grupos de acordo com a variável de interesse, neste caso com `proj`; aplicar a função ajuste, criada em 1, para cada um dos grupos  
> 3 - Resetar índice da data frame (transformar código do grupo de índice para coluna) e remover a coluna level_1 (derivada da criação da data frame no função). Estes comandos servem para gerar uma solução exatamente igual em todos os paradigmas
```python
def ajuste(df):
    y = df['y'].values
    X = np.vstack([df['x'].values, np.ones(len(y))]).T
    b1, b0 = np.linalg.lstsq(X, y, rcond=None)[0]
    return pd.DataFrame({'b0': [b0], 'b1': [b1]})

coef_fun = dados.groupby('proj').apply(ajuste)
coef_fun = coef_fun.reset_index().drop('level_1', axis = 1)
coef_fun
```
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>proj</th>
      <th>b0</th>
      <th>b1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.5</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>9.3</td>
      <td>-1.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>
</div>

<br>

 A [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) da biblioteca [pandas](https://pandas.pydata.org/)  geralmente é utilizada como etapa prévia da operação apply, porém pode ser perfeitamente utilizada para executar procedimentos em um loop for, em algumas situações pode até apresentar performance superior a sua utilização convencional: [groupby-apply](https://pandas.pydata.org/docs/user_guide/groupby.html), especialmente para funções que são definidas pelo usuário. O método [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) retorna um iterator que possibilita acessar o `k` nome do grupo e o `g` grupo de dados. O código apresenta um loop for em um processo de repetição para imprimir os dados na tela.
```python
for k, g in d.groupby('proj'):
    print('\n Grupo:', k, '\n', g)
```
<br>
<br>


## 3. Paradigma Vetorizado
O paradigma vetorizado (ou matricial) também utiliza processo de repetição implícita, em que os dados são preparados para serem executados por funções vetorizadas, tais como as disponibilizadas nas bibliotecas pandas, numpy e scipy. Os passos elementares são descritos a seguir:

Antes de inicializar o processo é necessário criar variáveis dummy. As variáveis dummy permitem o ajuste de um modelo para cada grupo (proj) em um único passo. A dummy é gerada no formato de matriz com n linhas, que correspondem à quantidade de observações totais e m colunas, que correspondem à quantidade de grupos, isto é, uma coluna para cada grupo. 
> 1 - Criar valores únicos dos códigos dos grupos, bem como os índices de início de cada grupo  
> 2 - Obter a quantidade de observações (n) e quantidade de grupos (m)   
> 3 - Criar array de zeros com a mesma quantidade de elementos da quantidade de observações  
> 4 - Substituir 0 por 1 em cada local de mudança de grupo   
> 5 - Criar os componentes básicos para construção da matriz de variáveis dummy: vetor de 1's (dados da matriz), vetor de índices de 0 a n (índices de linhas), e vetor com somatório acumulativo (índices de colunas)  
> 6 - Criação propriamente dita da matriz dummy, utilizando a função [csc_matrix](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html) do módulo [sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html) da biblioteca [scipy](https://www.scipy.org/)

```python
def dummy01(classe):
    unicos, idx = np.unique(classe, return_index = True)
    n, m = len(classe), len(unicos)
    id_arr = np.zeros(n, dtype=np.uint8)
    id_arr[idx[1:]] = 1
    csc_idx = (np.ones(n), (np.arange(n), id_arr.cumsum()))
    return csc_matrix(csc_idx, shape=(n, m), dtype = np.uint8)

print(dummy01(dados['proj'].values).todense())
```
   ```
    [[1 0 0]
     [1 0 0]
     [1 0 0]
     [1 0 0]
     [0 1 0]
     [0 1 0]
     [0 1 0]
     [0 1 0]
     [0 1 0]
     [0 0 1]
     [0 0 1]
     [0 0 1]
     [0 0 1]] 
```

> 1 - Ordenar os dados pela coluna de grupos. Essa etapa é necessária para construção de forma correta da matriz de variáveis dummy. O argumento inplace foi utilizado, que indica para a função de ordenação que o resultado deve substituir os dados originais.  
> 2 - Criar as variáveis dummy  
> 3 - Isolar a coluna referente à variável resposta `y`   
> 4 - Criar a matriz `X` <sub>`n x m`</sub> a partir da combinação por colunas da multiplicação das variáveis dummy pela variável explicativa `x` e multiplicação das variáveis dummy pela coluna constante, com valores iguais a 1. A matriz `X` apresenta `n` linhas (observações totais) e `m` colunas, que corresponde à quantidade de grupos * 2   
> 5 -  Ajustar o modelo `y = b0 + b1 * x` de forma semelhante aos paradigmas anteriores, mas desta vez a função [lsqr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsqr.html) será utilizada. Observe que está função pertence ao modulo sparse da scipy, e assim fornece suporte para matrizes esparsas   
> 6 - Salvar os coeficientes em uma data frame do pandas

```python
dados.sort_values('proj', inplace = True) # ordenar por grupos
dummy = dummy01(dados['proj'].values)
y = dados['y'].values
x = np.reshape(dados['x'].values, (-1 , 1))
X = hstack((dummy.multiply(x), dummy))
b1, b0 = np.split(linalg.lsqr(X, y)[0], 2)
coef_vet = pd.DataFrame({'proj': dados['proj'].unique(), 'b0': b0, 'b1': b1})
coef_vet
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>proj</th>
      <th>b0</th>
      <th>b1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.5</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>9.3</td>
      <td>-1.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>
</div>

<br>
Avaliação do ajuste pode ser feita com a função assert_array_almost_equal, que retorna erro se os dados forem diferentes de acordo com a especifícação da quantidade de casas decimais.  

```python
np.testing.assert_array_almost_equal(coef_vet.values, coef_fun.values, decimal=12)
```

A figura abaixo apresenta uma ilustração da etapa de organização dos dados e o resultado do ajuste do modelo pela função [lsqr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.lsqr.html).  

![alt text](https://raw.githubusercontent.com/gmarcatti/prog-python/main/img/ml_vetorizado.png)  

Obs 1: observe que a multiplicação da variável dummy pela coluna constante de 1's não é necessária, porém a etapa foi mantida na imagem por questões de didática.  
Obs 2: observe que as matrizes `Dummy` e `x` apresentam dimensões diferentes: `Dummy` <sub>`13 x 3`</sub> e `x` <sub>`13 x 1`</sub> , mesmo assim a operação de multiplicação pode ser executada, isso é possível devido à numpy transmitir a matriz `x` para cada uma das 3 colunas de `Dummy`. Essa operação recebe o nome de [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html), que além de simplificar o código, evita cópias desnecessárias dos dados.

As variáveis dummy, assim como todo o processo vetorizado, deve ser feito utilizando matrizes esparsas. Esse tipo de representação é econômico no uso de memória, além disso, o modulo [sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html) fornece funções especialmente desenvolvidas para trabalhar com matrizes enormes representas de forma esparsa. A figura a seguir ilustra o efeito da quantidade de grupos na performance (tempo de processamento) de cada um dos paradigmas de programação. Quanto menor o tempo melhor.
![alt text](https://raw.githubusercontent.com/gmarcatti/prog-python/main/img/imp_fun_vet.png)

Obs: Apenas as soluções destacadas com setas são apresentadas no documento.  