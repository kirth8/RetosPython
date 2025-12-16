print("========================================================================")
print("Invertir palabras en una frase")
print("Dada una frase, invierte cada palabra individualmente")
print("pero mantiene el orden de las palabras.")
print("")
print("Ejemplo:")
print("entrada = 'hola mundo python'")
print("Salida: 'aloh odnum nohtyp'")
print("")
print("Restricciones:")
print("- No usar slicing ([::-1])")
print("- No usar split() ni join()")
print("- No usar funciones avanzadas")
print("- Solo ciclos, índices, comparaciones y variables auxiliares")
print("- Recorrer la cadena carácter por carácter")
print("========================================================================")

entrada = input("Escribe una frase: ")

def invertirFrase(entrada):
    aux = ""
    contador = 0
    salida = ""
    salidaR= ""
    for i in entrada:
        contador += 1

        if i != " ":
            aux = aux + i

        if i == " " or contador == len(entrada):
            
            for j in aux:
                salida = j + salida
                
            if contador == len(entrada):
                salidaR = salidaR + salida
            else:
                salidaR = salidaR + salida + " "
                aux = ""
                salida = ""
            
    print(salidaR)

invertirFrase(entrada)

print("========================================================================")
