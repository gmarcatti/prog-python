# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 07:35:07 2021

@author: Gustavo Eduardo Marcatti
"""
###------------------------------------------------------------------###
#---- Operações básicas
###------------------------------------------------------------------###
a = 2
b = 3
a + b
a * b

###------------------------------------------------------------------###
#---- Imprimir na tela
###------------------------------------------------------------------###
a + b
print(a + b)

print("Seja bem vindo!")

###------------------------------------------------------------------###
#---- Executar funções
###------------------------------------------------------------------###
import math
math.log(2)
math.log(2, 3)
math.log(2)
math.log(2, math.e)
# math.log(, math.e) # erro

###------------------------------------------------------------------###
#---- Criar variáveis
###------------------------------------------------------------------###
log_valor = math.log(2)
resultado_final = log_valor * 45.1
resultado_final
print(resultado_final)

obj1 = math.sqrt(25)
obj2 = math.sqrt(12)

nome = "Eduardo"

###------------------------------------------------------------------###
#---- Criar funções
###------------------------------------------------------------------###

#---- Exemplo de boas vindas ------------------------------------------#
# 1: sem argumentos e sem retorno
def boas_vindas1():
    print("Seja bem vindo!")

boas_vindas1()

# 2: com argumento
def boas_vindas2(nome):
    print("Seja bem vindo", nome, "!")

boas_vindas2("Fulano")

# 3: com argumento padrão
def boas_vindas3(nome = "aluno"):
    print("Seja bem vindo", nome, "!")

boas_vindas3()
boas_vindas3("Fulano")

#---- Exemplo análise econômica de projetos ---------------------------#
# Exemplo análise econômica de projetos
# 4: com retorno
# Com repetição de código
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

# com função
def aval_eco(receita, custo):
    lucro = receita - custo
    return(lucro)
    
proj1 = aval_eco(6000, 4000)
proj2 = aval_eco(9000, 5000)
proj3 = aval_eco(6000, 6500)

lucro_geral = proj1 + proj2 + proj3
lucro_geral

# bloco de execução inicializado com :
# e encerrado com o fim da indentação 
def funcao():
    a = 3
    b = 3
    cv = a * b
    return(cv)

funcao()


