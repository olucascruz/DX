class Calculadora:
    def __init__(self) -> None:
        pass

    
    def convert_float(self, num_1 , num_2) -> float:
        """ Converte os números 'num_1' e 'num_2' para o tipo float caso não seja possivel retorna a string 'Error' """
        try:
            num_1, num_2 = float(num_1), float(num_2)
        except Exception:
            return "ERROR"
        
        return num_1, num_2

    
    
    def soma(self, num_1, num_2) -> float:
        """ Soma num_1 e num_2 e retorna o resultado """
        num_1, num_2 = self.convert_float(num_1, num_2)
       
        return num_1 + num_2
    
    def subtracao(self, num_1, num_2) -> float:
        num_1, num_2 = self.convert_float(num_1, num_2)
        
        return num_1 - num_2
    
    def divisao(self, dividendo, divisor) -> float:
        """ Divide dividendo pelo divisor e retorna o resultado """
        dividendo, divisor = self.convert_float(dividendo, divisor) 
        
        return dividendo / divisor

    def multiplicacao(self, fator_1, fator_2) -> float:
        """ Multiplica fator_1 por fator_2 e retorna o resultado """
        fator_1, fator_2 = self.convert_float(fator_1, fator_2)

        return fator_1 * fator_2
    
    def potencia(self, base, expoente) -> float:
        """ retorna num_1 elevado a num_2 """
        base, expoente = self.convert_float(base, expoente)
        
        return base ** expoente
    

    def radiciação(self, radicando, indice) -> float:
        """Tira a raiz de num_1 por num_2 """
        radicando, indice = self.convert_float(radicando, indice)
        
        try:
            raiz = radicando ** (1/indice)

        except Exception:
            return "ERROR: raiz não existe"
        
        return raiz
    
    def converte_bin_to_int(self, n:bin) -> int:
        """Converte um número em binário"""
        return int(n, 2)

    def converte_int_to_bin(self, n:int) -> bin:
        """Converte um número em binário"""
        return bin(n)