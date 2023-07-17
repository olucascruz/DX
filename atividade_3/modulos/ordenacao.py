import sorting




def ordenacao(lista:list, algoritmo="Bubble"):
    """Recebe uma lista e um algoritmo de ordenação e retorna a lista ordenada com este algoritmo,
      os algoritmos validos são: 'Bubble', 'Quick', 'Merge', 'Tim', por padrão o algoritmo é 'Bubble' """
    

    if algoritmo == "Bubble":
        ord = sorting.bubble(lista)
        return ord
    if algoritmo == "Quick":
        ord = sorting.quick(lista)
        return ord
    if algoritmo == "Merge":
        ord = sorting.merge(lista)
        return ord
    if algoritmo == "Tim":
        lista.sort()
        return lista

