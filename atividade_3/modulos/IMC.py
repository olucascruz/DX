from .calculadora import Calculadora

def calc_IMC(altura, peso):
    calc = Calculadora()
    imc = calc.divisao(peso, calc.multiplicacao(altura, altura))
    return imc


def classifica_IMC(imc):
    if imc < 18.50:
        return f' imc: {imc} -> Magreza'
    elif 24.99 >= imc >= 18.50:
        return f' imc: {imc} -> Normal'
    elif 29.99 >= imc >= 25:
        return f' imc: {imc} -> Sobrepeso'
    elif 39.99 >= imc >= 30:
        return f' imc: {imc} -> Obesidade'
    else:
        return f' imc: {imc} -> Obesidade Grave'

