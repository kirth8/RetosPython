print("========================================================================")
print("Eliminar caracteres duplicados de una cadena")
print("Dada una cadena de texto, crea una nueva cadena que contenga")
print("solo la primera aparición de cada carácter,")
print("manteniendo el orden original.")
print("")
print("Ejemplo:")
print("entrada = 'programacion'")
print("Salida: 'progamin'")
print("")
print("Restricciones:")
print("- No usar set()")
print("- No usar funciones avanzadas")
print("- No usar replace()")
print("- Solo ciclos, comparaciones y variables auxiliares")
print("- Recorrer la cadena carácter por carácter")
print("========================================================================")
entrada = input("Escribe una palabra: ")
verificar = {}

def eliminarCarateresduplicados(entrada):
    salida = ""

    for i in entrada:
        if i not in verificar:
            verificar[i] = 1
        else:
            verificar[i] += 1
    
    for j in verificar:
        salida = salida + j

    print(verificar)
    print(salida)

eliminarCarateresduplicados(entrada)


print("========================================================================")