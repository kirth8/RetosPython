print("========================================================================")
print("Contar cuántas veces aparece cada letra en una palabra")
print("Dada una palabra, debes contar cuántas veces aparece cada letra y mostrar el resultado.")
print("Ejemplo\n\ninput:  'banana'\n\noutput:\nb->1\na->3\nn->2\n\n")
print("Restricciones:\n-No usar collections.Counter\n-No usar .count()\n-No usar diccionarios preconstruidos (puedes crear uno tú manualmente)")
print("-Solo usar:\n--ciclos\n--índices\n--comparaciones\n--variables auxiliares\n--estructuras básicas como listas o diccionarios simples que TÚ llenes")
print("========================================================================\n")

Entrada = input("Escribe una palabra: ")
aux = 0 
diccionario = {"a":0, "b":0,"c":0, "d":0,"e":0, "f":0,"g":0, "h":0,"i":0, "j":0,"k":0, "l":0,"m":0, 
               "n":0,"ñ":0, "o":0,"p":0, "q":0,"r":0, "s":0,"t":0, "u":0,"v":0, "w":0,"x":0, "y":0,"z":0}

contador = {}

def contarLetras(Entrada, contador):
    for letra in Entrada:
        if letra not in contador:
            contador[letra] = 1
        else:
            contador[letra] += 1
    
    for letra in contador:
        print(letra, "->", contador[letra])

contarLetras(Entrada, contador)


print("========================================================================\n")