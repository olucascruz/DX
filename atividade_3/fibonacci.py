

def fib_impares():
    list_imapares = [1, 1]
    n = int(input("Digite até qual termo deseja armazenar os números impares de fibonacci: "))
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

