from .ordenacao import ordenacao


def fib_impares(n:int) -> list:
    try:
        n = int(n)
    except Exception:
        print("Argumento deve ser um número")
    
    """Recebe um número e retorna os impares da sequencia de fibonacci até a posição do número recebido"""
    list_imapares = [1, 1]
    ultimo=1
    penultimo=1

    if (n==1) or (n==2):
        print("1")
    else:
        for count in range(2,n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            if(termo % 2 != 0):
                list_imapares.append(termo)

    return list_imapares

def ordene(lista:list, crescente=True) -> list:
    """Recebe uma lista e retorna ela ordenada. Parâmetro opcional 'crescente' -> por padrão é True """

    if(crescente): lista.sort()
    else: lista.sort(reverse=True)

    return lista

def soma_itens_lista(lista:list) -> float:
    """Soma todos os valores númericos de uma lista"""

    n = 0
    for i in lista: 
        try:
            n += i
        except Exception:
            continue
    
    return n 

def maior(lista:list):
    """Recebe uma lista como argumento e retorna o maior valor"""
    return ordenacao(lista=lista, algoritmo="Tim")[-1]

def menor(lista:list):
    """Recebe uma lista como argumento e retorna o menor valor"""
    return ordenacao(lista=lista, algoritmo="Tim")[-1]


def concatena_lista(lista_1:list, lista_2:list, crescente:bool=True) -> list:
    """Concatena duas lista, parâmetro opcional 'crescente', por padrão é True"""
    lista_3 = lista_1 + lista_2
    
    if crescente: lista_3 = ordene(lista_3)    
    else: lista_3 = ordene(lista_3, crescente=False)
    
    return lista_3