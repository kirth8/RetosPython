print("========================================================================\n\n")
print("Verificar si una palabra es un palíndromo\n")
print("Una palabra es palíndroma si se lee igual de izquierda a derecha y de derecha a izquierda.\n")
print("Ejemplo:\n\n")
print("'ana'->True\n'reconocer'->True\n'python'->False\n\n")
print("Restricciones:\n")
print("-No usar slicing ([::-1])\n-No usar funciones como reversed() ni .reverse()\n-Solo:")
print("--ciclos\n--índices\n--comparaciones\n--variables auxiliares")
print("========================================================================\n")

aux=0

Entrada = input("Escribe una palabra: ")
Tamaño = len(Entrada) - 1

def verficarPalindrono(Entrada, Tamaño, aux):
    while(aux < Tamaño):
        if Entrada[Tamaño] == Entrada[aux]:
            Tamaño-= 1
            aux+= 1
            
        else:
            print("False")
            return
    
    print("True")

    # for num in range(Tamaño):
    #     if Entrada[Tamaño] == Entrada[aux]:
    #         Tamaño-= 1
    #         aux+= 1

    #         if aux > Tamaño:
    #             print("True")
    #             break
    #         elif Entrada[Tamaño] != Entrada[aux]:
    #             print("False")
    #             break
    #     else:
    #         print("False")
    #         break


verficarPalindrono(Entrada, Tamaño, aux)

print("========================================================================\n\n")