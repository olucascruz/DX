from calculadora import Calculadora

def calc_IMC(altura, peso):
    calc = Calculadora()
    imc = calc.divisao(peso, calc.multiplicacao(altura, altura))
    return imc


def classifica_IMC(imc):
    if imc < 18.50:
        return "Magreza"
    elif imc >= 18.50 and  imc <=24.99:
        return 'Normal'
    elif imc >= 25 and  imc <=29.99:
        return 'Sobrepeso'
    elif imc >= 30 and  imc <=39.99:
        return 'Obesidade'
    else:
        return 'Obesidade Grave'

