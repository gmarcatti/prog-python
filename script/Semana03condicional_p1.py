# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:05:17 2021

@author: Gustavo Eduardo Marcatti
"""

###------------------------------------------------------------------###
#---- Exemplo 1 Avaliação econômica
###------------------------------------------------------------------###

###------------------------------------------------------------------###
#---- Condicional if
###------------------------------------------------------------------###
receita = 7000
custo = 8000
resultado = receita - custo
if resultado > 0:
    print("Projeto com lucro!")

###------------------------------------------------------------------###
#---- Condicional if-else
###------------------------------------------------------------------###
receita = 8000
custo = 8000
resultado = receita - custo
if resultado > 0:
    print("Projeto com lucro de R$", resultado)
else:
    print("Projeto com prejuízo de R$", abs(resultado))

###------------------------------------------------------------------###
#---- Condicional if-elif-else
###------------------------------------------------------------------###
receita = 7000
custo = 9000
resultado = receita - custo
if resultado > 0:
    print("Projeto com Lucro de R$", resultado)
elif resultado == 0:
    print("Projeto sem lucro... e sem prejuízo")
else:
    print("Projeto com Prejuízo de R$", abs(resultado))

#---- Criar função ----------------------------------------------------#
def aval_eco(receitas, custos):
    resultado = receitas - custos
    if resultado > 0:
        print("Projeto com Lucro de R$", resultado)
    elif resultado == 0:
        print("Projeto sem lucro... e sem prejuízo")
    else:
        print("Projeto com Prejuízo de R$", abs(resultado))
    return(resultado)

proj1 = aval_eco(9000, 5000)
proj2 = aval_eco(5000, 5000)
proj3 = aval_eco(4500, 5000)

print("Total R$", proj1 + proj2 +proj3)

###------------------------------------------------------------------###
#---- Exemplo 2 Decisão de expansão de área
###------------------------------------------------------------------###
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

#---- Criar função ----------------------------------------------------#
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

exp_area(4000, 5000, 200)
exp_area(6000, 5000, 200)
exp_area(9000, 5000, 200)
exp_area(11000, 5000, 200)