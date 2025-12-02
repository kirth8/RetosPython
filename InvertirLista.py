print("========================================================================\n")
print("Invertir una lista SIN usar slicing ni funciones avanzadas\n")
print("Dada una lista, devuelve la misma lista pero al revés.\nEjemplo:\n\n")
print("input:  [1, 2, 3, 4, 5]\n\noutput: [5, 4, 3, 2, 1]\n\n")
print("Restricciones:\n-No usar [::-1]\n-No usar .reverse()\n-No usar reversed()" \
"\n-Solo ciclos, variables auxiliares e índices\n-Puedes crear una nueva lista " \
"para almacenar el resultado")
print("========================================================================\n\n")

listaA = [1, 2, 3, 4, 5]

def inversionLista(listaA):
    listaB= []
    num = len(listaA) -1

    while num >= 0:
        listaB.append(listaA[num])
        num-= 1

    print(listaB)

            
inversionLista(listaA)

print("========================================================================\n")