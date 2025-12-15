print("========================================================================")
print("Encontrar el carácter que más se repite")
print("Dada una cadena de texto, encuentra el carácter que aparece más veces.")
print("Si hay empate, puedes devolver cualquiera.")
print("")
print("Ejemplo:")
print("entrada = 'programacion'")
print("Salida posible: 'o'")
print("")
print("Restricciones:")
print("- No usar collections.Counter")
print("- No usar set()")
print("- No usar funciones avanzadas")
print("- Solo ciclos, comparaciones, diccionarios y variables auxiliares")
print("========================================================================")

entrada = "programacion"

def caracterMasRepetido(entrada):
    verificacion = {}
    letra = None
    mayor = None

    for i in entrada:
        if i in verificacion:
            verificacion[i] +=1
        else:
            verificacion[i] = 1
    
    for j in entrada:    
        valor = verificacion[j]

        if  mayor is None or valor > mayor:
            letra = j
            mayor = verificacion[j]
            
    print("La letra ", letra, " tiene una repeticion de ", mayor)

caracterMasRepetido(entrada)

print("========================================================================")
