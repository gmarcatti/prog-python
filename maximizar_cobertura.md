# Localização - Alocação: O Problema de maximizar a cobertura

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
dist_matriz
```
    
      dist_matriz = infra.geometry.apply(lambda g: antenas.distance(g))
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>cod_antena</th>
      <th>a1</th>
      <th>a2</th>
      <th>a3</th>
      <th>a4</th>
      <th>a5</th>
      <th>a6</th>
      <th>a7</th>
      <th>a8</th>
      <th>a9</th>
    </tr>
    <tr>
      <th>Cod_proj</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>182717.325777</td>
      <td>90736.935322</td>
      <td>13956.693660</td>
      <td>90411.290832</td>
      <td>67867.349495</td>
      <td>75798.424238</td>
      <td>35909.029358</td>
      <td>264971.770873</td>
      <td>148224.852598</td>
    </tr>
    <tr>
      <th>40</th>
      <td>151750.541574</td>
      <td>160798.513512</td>
      <td>82930.415350</td>
      <td>100944.305358</td>
      <td>115575.513862</td>
      <td>34924.440998</td>
      <td>37312.825792</td>
      <td>220987.285865</td>
      <td>114695.205596</td>
    </tr>
    <tr>
      <th>150</th>
      <td>71991.908453</td>
      <td>222842.725681</td>
      <td>175139.917888</td>
      <td>87227.245537</td>
      <td>130292.700800</td>
      <td>140212.876696</td>
      <td>183270.104091</td>
      <td>146398.638567</td>
      <td>83197.297754</td>
    </tr>
    <tr>
      <th>5350</th>
      <td>204837.721622</td>
      <td>46870.902514</td>
      <td>41216.646488</td>
      <td>99663.530660</td>
      <td>49170.032219</td>
      <td>119890.062667</td>
      <td>90951.603153</td>
      <td>292067.835877</td>
      <td>175456.192506</td>
    </tr>
    <tr>
      <th>210</th>
      <td>76480.991643</td>
      <td>210155.899604</td>
      <td>133950.674098</td>
      <td>86135.949454</td>
      <td>132558.922485</td>
      <td>51805.526392</td>
      <td>107350.686860</td>
      <td>143074.440035</td>
      <td>41563.416855</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7050</th>
      <td>164987.533416</td>
      <td>118815.763186</td>
      <td>40589.296620</td>
      <td>85341.940346</td>
      <td>80931.702403</td>
      <td>50658.592242</td>
      <td>14880.801969</td>
      <td>243759.503784</td>
      <td>128956.998196</td>
    </tr>
    <tr>
      <th>7130</th>
      <td>118234.208850</td>
      <td>147376.343114</td>
      <td>71726.783210</td>
      <td>49756.003671</td>
      <td>76220.781518</td>
      <td>22982.433389</td>
      <td>57770.738773</td>
      <td>199172.496024</td>
      <td>82776.819260</td>
    </tr>
    <tr>
      <th>7140</th>
      <td>150564.023546</td>
      <td>102283.404711</td>
      <td>59089.926744</td>
      <td>44667.660640</td>
      <td>10116.523683</td>
      <td>90121.533728</td>
      <td>91612.137354</td>
      <td>238690.367938</td>
      <td>124403.418857</td>
    </tr>
    <tr>
      <th>7200</th>
      <td>95850.758582</td>
      <td>158711.187329</td>
      <td>89913.034178</td>
      <td>28529.334871</td>
      <td>74174.939555</td>
      <td>45138.120846</td>
      <td>85745.930244</td>
      <td>180996.474519</td>
      <td>63725.191099</td>
    </tr>
    <tr>
      <th>7210</th>
      <td>86773.585887</td>
      <td>203176.448262</td>
      <td>159503.085331</td>
      <td>73591.877779</td>
      <td>111569.427353</td>
      <td>134141.254303</td>
      <td>172354.182396</td>
      <td>166017.739963</td>
      <td>89876.420901</td>
    </tr>
  </tbody>
</table>
<p>129 rows × 9 columns</p>
</div>



Considerar apenas os pontos da matriz em que a distância é menor do que o alcance da respectiva antena


```python
cond_dist = dist_matriz < antenas['alcance_m']
dist_alcance = dist_matriz[cond_dist]
dist_alcance
```





</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>cod_antena</th>
      <th>a1</th>
      <th>a2</th>
      <th>a3</th>
      <th>a4</th>
      <th>a5</th>
      <th>a6</th>
      <th>a7</th>
      <th>a8</th>
      <th>a9</th>
    </tr>
    <tr>
      <th>Cod_proj</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>13956.693660</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>34924.440998</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>150</th>
      <td>71991.908453</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5350</th>
      <td>NaN</td>
      <td>46870.902514</td>
      <td>41216.646488</td>
      <td>NaN</td>
      <td>49170.032219</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>210</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41563.416855</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7050</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>40589.296620</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>14880.801969</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7130</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>49756.003671</td>
      <td>NaN</td>
      <td>22982.433389</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7140</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>44667.660640</td>
      <td>10116.523683</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7200</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28529.334871</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7210</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>129 rows × 9 columns</p>
</div>



Converter a matriz formato padrão com i pontos de estruturas e j antenas (i *x* j) em uma matriz com i * j linhas e 3 colunas (pontos de estrutura, antenas e distâncias).


```python
dist_alcance = dist_alcance.stack().reset_index()
dist_alcance
```

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cod_proj</th>
      <th>cod_antena</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>30</td>
      <td>a3</td>
      <td>13956.693660</td>
    </tr>
    <tr>
      <th>1</th>
      <td>40</td>
      <td>a6</td>
      <td>34924.440998</td>
    </tr>
    <tr>
      <th>2</th>
      <td>150</td>
      <td>a1</td>
      <td>71991.908453</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5350</td>
      <td>a2</td>
      <td>46870.902514</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5350</td>
      <td>a3</td>
      <td>41216.646488</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>218</th>
      <td>7130</td>
      <td>a4</td>
      <td>49756.003671</td>
    </tr>
    <tr>
      <th>219</th>
      <td>7130</td>
      <td>a6</td>
      <td>22982.433389</td>
    </tr>
    <tr>
      <th>220</th>
      <td>7140</td>
      <td>a4</td>
      <td>44667.660640</td>
    </tr>
    <tr>
      <th>221</th>
      <td>7140</td>
      <td>a5</td>
      <td>10116.523683</td>
    </tr>
    <tr>
      <th>222</th>
      <td>7200</td>
      <td>a4</td>
      <td>28529.334871</td>
    </tr>
  </tbody>
</table>
<p>223 rows × 3 columns</p>
</div>



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



## 3. Solução aproximada utilizando procedimento guloso

Preparação dos dados para execução do algoritmo. Dicionário (dict) em que a chave (key) é o código das antenas e os valores (value) é um conjunto (set) com os pontos de infraestruturas alcançados por cada uma das antenas


```python
antena_uni = dist_alcance['cod_antena'].unique()
antena_infra = {}
for ant in antena_uni:
    infra_i = set(dist_alcance[dist_alcance['cod_antena'] == ant]['Cod_proj'])
    antena_infra[ant] = infra_i

antena_infra
```




    {'a3': {30,
      250,
      370,
      1170,
      1210,
      1290,
      1330,
      2200,
      2270,
      2352,
      2420,
      2595,
      3550,
      3940,
      3950,
      4090,
      4210,
      4880,
      5020,
      5350,
      5400,
      5490,
      5740,
      5790,
      5890,
      6010,
      6140,
      6255,
      6400,
      6630,
      6760,
      7050},
     'a6': {40,
      250,
      870,
      1020,
      1630,
      1670,
      2170,
      2190,
      2330,
      2820,
      4830,
      4880,
      5080,
      5210,
      5230,
      5310,
      6150,
      6380,
      6570,
      6600,
      6850,
      7130},
     'a1': {150,
      330,
      440,
      460,
      610,
      680,
      690,
      1590,
      1620,
      1960,
      2130,
      2290,
      2500,
      2840,
      2850,
      3260,
      3670,
      3840,
      3860,
      3980,
      4020,
      4080,
      4160,
      4540,
      4570,
      4660,
      4940,
      4950,
      5010,
      5130,
      5540,
      5580,
      5590,
      5620,
      5860,
      5940,
      6000,
      6070,
      6290,
      6560,
      6730,
      6750,
      6790,
      6900},
     'a2': {1210, 1600, 2352, 3770, 3940, 3950, 5350, 5890, 6760},
     'a5': {310,
      370,
      550,
      1010,
      1170,
      1210,
      1330,
      2200,
      2400,
      2420,
      2490,
      2530,
      2595,
      3950,
      4210,
      4390,
      4820,
      4900,
      5350,
      5790,
      6140,
      6255,
      6630,
      6920,
      7140},
     'a9': {210,
      330,
      440,
      460,
      680,
      690,
      870,
      1590,
      1630,
      1960,
      2130,
      2190,
      2290,
      2330,
      2500,
      2840,
      2850,
      2880,
      3260,
      3670,
      3980,
      4020,
      4080,
      4160,
      4570,
      4660,
      4950,
      5010,
      5130,
      5540,
      5580,
      5620,
      5630,
      6070,
      6290,
      6570,
      6730,
      6790,
      6900,
      6990},
     'a4': {310,
      460,
      550,
      1020,
      1170,
      1530,
      1670,
      2190,
      2290,
      2400,
      2490,
      2880,
      2900,
      3260,
      3800,
      3840,
      4210,
      4220,
      4390,
      4670,
      4820,
      4830,
      4880,
      4900,
      5130,
      5410,
      5630,
      5840,
      6140,
      6150,
      6380,
      6850,
      6900,
      6990,
      7130,
      7140,
      7200},
     'a7': {570, 2270, 3550, 5020, 5210, 5490, 5500, 5740, 6010, 7050},
     'a8': {3860, 4540, 5590, 5930}}



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
    
