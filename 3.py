def Impar(tamaño):
    c = 0
    lista = []
    while (c < tamaño):
        num = eval(input("Numero {}: ".format(c)))
        lista.insert(c,num)
        c = c+1
    c = 0
    while (c < tamaño):
        if (c % 2 == 0):
            del lista[c]       
        c = c+1
    return lista

tamaño = int(input("De que tamaño desea la lista: "))
print(Impar(tamaño))
