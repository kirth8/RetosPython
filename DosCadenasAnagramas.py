print("========================================================================")
print("Verificar si dos cadenas son anagramas")
print("Dos cadenas son anagramas si contienen las mismas letras")
print("con la misma cantidad, pero en diferente orden.")
print("")
print("Ejemplo 1:")
print("cadena1 = 'roma'")
print("cadena2 = 'amor'")
print("Salida: True")
print("")
print("Ejemplo 2:")
print("cadena1 = 'hola'")
print("cadena2 = 'halo'")
print("Salida: True")
print("")
print("Ejemplo 3:")
print("cadena1 = 'python'")
print("cadena2 = 'java'")
print("Salida: False")
print("")
print("Restricciones:")
print("- No usar sorted()")
print("- No usar collections.Counter")
print("- No usar set()")
print("- No usar funciones avanzadas")
print("- Solo ciclos, comparaciones, diccionarios o listas creadas por ti")
print("========================================================================")

A1 = 'hola'
A2 = 'halo'

B1 = 'roma'
B2 = 'amor'

C1 = 'python'
C2 = 'java'

def verificarAnagramas(string1, string2):
    diccionario1 = {}
    diccionario2 = {}

    #Se añade este condicional para optimizar el codigo, ya que un anagrama en 
    # dos diferentes strings siempre van a tener el mismo tamaño
    if len(string1) != len(string2):
        print("False")
        return

    for i in string1:
        if i in diccionario1:
            diccionario1[i] +=1
        else:
            diccionario1[i] = 1

    for i in string2:
        if i in diccionario2:
            diccionario2[i] +=1
        else:
            diccionario2[i] = 1

    return diccionario1 == diccionario2

print(verificarAnagramas(B1, B2))

print("========================================================================")
