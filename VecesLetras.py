print("========================================================================")
print("Contar cuántas veces aparece cada letra en una palabra")
print("Dada una palabra, debes contar cuántas veces aparece cada letra y mostrar el resultado.")
print("Ejemplo\n\ninput:  'banana'\n\noutput:\nb->1\na->3\nn->2\n\n")
print("Restricciones:\n-No usar collections.Counter\n-No usar .count()\n-No usar diccionarios preconstruidos (puedes crear uno tú manualmente)")
print("-Solo usar:\n--ciclos\n--índices\n--comparaciones\n--variables auxiliares\n--estructuras básicas como listas o diccionarios simples que TÚ llenes")
print("========================================================================\n")

Entrada = input("Escribe una palabra: ")
aux = 0

def contarLetras(Entrada, aux):
    listaLetras = []
    for letra in Entrada:
        tupla = (letra, aux)
        listaLetras.append(tupla)
        
        cont = len(listaLetras) 
        
        while(cont != 0):
            cont -=1
            print("Bandera 1")
            if (listaLetras[cont][1] > 0 ):
                listaLetras[cont][1] += 1
            print(listaLetras)
        
        
        
    # print(len(listaLetras))
    # print(listaLetras)
    # print(listaLetras[2][0])

contarLetras(Entrada, aux)

print("========================================================================\n")