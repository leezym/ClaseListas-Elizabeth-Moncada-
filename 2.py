def Cambiar(tamaño):
    c = 0
    lista = []
    lista2 = []
    while (c < tamaño):
        num = eval(input("Numero {}: ".format(c+1)))
        lista.insert(c,num)
        c = c+1

    c = 0
    while (c < tamaño):
        if (lista[c] < 0):
            lista2.insert(c,0)
        else:
            lista2.insert(c,lista[c])
        c = c+1
    print("Original: {}\nResultado: {}".format(lista, lista2))

tamaño = int(input("De que tamaño desea la lista: "))
Cambiar(tamaño)
