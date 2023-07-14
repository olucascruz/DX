from IMC import calc_IMC, classifica_IMC
from salario import salario
from fibonacci import fib_impares


print("IMC --------------------------")
imc = calc_IMC()
print(classifica_IMC(imc))
print("------------------------------")


print("SALÁRIO ----------------------")
salario()
print(classifica_IMC(imc))
print("------------------------------")

print("FIBONACCI IMPARES-------------")
print(fib_impares())
print("------------------------------")
