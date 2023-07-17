import random
from modulos.IMC import calc_IMC, classifica_IMC
from modulos.salario import salario
from modulos.lista import fib_impares, ordene, maior, menor, concatena_lista, soma_itens_lista
from modulos.ordenacao import ordenacao
from datetime import datetime
from modulos.calculadora import Calculadora

calc = Calculadora()

print("IMC --------------------------")
imc = calc_IMC(1.73, 90)
print(classifica_IMC(imc))
print("------------------------------")


print("SALÁRIO ----------------------")
salario()
print("------------------------------")

print("FIBONACCI IMPARES-------------")
print(fib_impares(10))
print("------------------------------")


lista = list()
lista_2 = list()
for _ in range(30): 
    lista.append(random.randint(1, 30))
    lista_2.append(random.randint(1, 30))

print(f"Lista 1: {lista}")
print(f"Lista 2: {lista_2}")

print()
# 1 

lista_ordenada = ordene(lista)
lista_ordenada_decres = ordene(lista, crescente=False)

print(lista_ordenada)
print(lista_ordenada_decres)

print()

# Desafio
algoritimos = ["Bubble", "Merge", "Quick", "Tim"]

for algoritmo in algoritimos:
    print(f"{algoritmo} \n")
    inicio = datetime.now().second
    print(ordenacao(lista, algoritmo))
    print("-------------------")
    print(f"Tempo de execução {datetime.now().second - inicio} \n")


# 2

print(f"Elementos somados: {soma_itens_lista(lista)}")

# 3 

print()
print("Maior e menor elemento da lista 1")
print(maior(lista))
print(menor(lista))

# Extra

print("concatenação de listas crescente e decrescente")

print(concatena_lista(lista, lista_2))

print()
print(concatena_lista(lista, lista_2, crescente=False))

print()

inteiro = 45

binario = calc.converte_int_to_bin(inteiro)

print(inteiro) 
print(binario)
print(calc.converte_bin_to_int(binario))





