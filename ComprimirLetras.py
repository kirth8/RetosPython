print("========================================================================")
print("Comprimir una cadena (Run Length Encoding básico)")
print("Dada una cadena de texto, debes comprimirla contando cuántas veces se " \
"repite cada carácter de forma consecutiva.")
print("Ejemplo:\n")
print("entrada = 'aaabbcddd'\n")
print("Salida: a3b2c1d3\n")
print("Restricciones")
print("- No usar librerías\n- No usar funciones avanzadas\n- Solo ciclos, comparaciones y variables auxiliares" \
"\n- Recorrer la cadena carácter por carácter")
print("========================================================================")

entrada = 'aaabbcddd'

def contarLetras(entrada):
    salida = ' ' 
    aux= 0

    for i in entrada:
        if i == salida[-1]:
            aux += 1
            
        else:
            salida += str(aux)
            aux = 1
            salida += i
            
    salida += str(aux)

    print(salida)

contarLetras(entrada)

print("========================================================================")