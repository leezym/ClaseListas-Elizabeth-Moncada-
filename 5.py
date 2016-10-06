def InsertarLista(tamaño):
    c = 0
    lista = []     
    while (c < tamaño):
        num = eval(input("Numero {}: ".format(c+1)))
        lista.insert(c,num)
        c = c+1
    print("Original: ",lista)
    Mayor(tamaño, lista)
    Cambiar(tamaño, lista)
    print(Impar(tamaño, lista))
        
def Mayor(tamaño, lista):
    mayor = lista[0]
    c = 0
    while (c < tamaño):
        if (mayor < lista[c]):
            mayor = lista[c]
        c = c+1
    print("El mayor número de la lista es: ", mayor)

def Cambiar(tamaño, lista):    
    lista2 = []
    c = 0
    while (c < tamaño):
        if (lista[c] < 0):
            lista2.insert(c,0)
        else:
            lista2.insert(c,lista[c])
        c = c+1
    print("Cambiando los negativos por cero: ", lista2)

def Impar(tamaño, lista):
    lista2 = []
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
InsertarLista(tamaño)

