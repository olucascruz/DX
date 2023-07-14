import time
from calculadora import Calculadora

def salario():
  
    calc = Calculadora()
    salario = input("Digite o salário: ")
    
    while True:
        print("-----------------------------------------")
        print(f"O salario atual é {salario}")
        print("-----------------------------------------")
        print("carregando...")
        time.sleep(4)

        print("Deseja adicionar um bonus ao salário? - Digite 1")
        print("Deseja descontar um valor do salário? - Digite 2")
        print("Deseja adicionar um novo valor ao salário? - Digite 3")
        print("Deseja finalizar operação? - Digite 4")



        print()

        operacao = input("Digite -> ")
        
        if(operacao == "1"):
            bonus = input("Digite o bonus: ")
            salario = calc.soma(salario, bonus)
        
        elif operacao == "2":
            bonus = input("Digite o bonus: ")
            salario = calc.subtracao(salario, bonus)    
        
        elif operacao == "3":
            salario = input("Digite o salário")
        
        elif operacao == "4":
            print("-----------------------------------------")
            print(f"O salario atual é {salario}")
            print("-----------------------------------------")
            print("OPERAÇÃO FINALIZADA")

            return salario
        else:
            print("Operação não existe")
            print()
            print("Aguarde")

            time.sleep(5)

    

salario()