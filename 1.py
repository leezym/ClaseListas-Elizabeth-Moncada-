def Mayor(tamaño):
    c = 0
    lista = []     
    while (c < tamaño):
        num = eval(input("Numero {}: ".format(c+1)))
        lista.insert(c,num)
        c = c+1

    mayor = lista[0]
    c = 0
    while (c < tamaño):
        if (mayor < lista[c]):
            mayor = lista[c]
        c = c+1
    return mayor

tamaño = int(input("De que tamaño desea la lista: "))
print(Mayor(tamaño))
