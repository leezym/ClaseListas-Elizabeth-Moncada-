def Impar(tamaño):
    c = 0
    lista = []
    lista2 = []
    while (c < tamaño):
        num = eval(input("Numero {}: ".format(c)))
        lista.insert(c,num)
        c = c+1
    c = 0
    x = 0
    while (c < tamaño):
        if (c % 2 == 0):
            print("Eliminando el elemento {}, con índice {}".format(lista[c], c))
        else:
            lista2.insert(x,lista[c])
            x = x+1
        c = c+1
    return lista2            

tamaño = int(input("De que tamaño desea la lista: "))
print(Impar(tamaño))
