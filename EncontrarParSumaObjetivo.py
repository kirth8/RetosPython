print("========================================================================")
print("Encontrar el par de números que suman un objetivo")
print("Dada una lista de números enteros y un número objetivo, determina si existe un par de " \
"números distintos en la lista cuya suma sea igual al objetivo.\n")
print("Ejemplo 1\n")
print("lista = [2, 7, 11, 15]\nobjetivo = 9\n\nSalida: True  # (2 + 7)\n")
print("Ejemplo 2\n")
print("lista = [3, 5, 1, 7]\nobjetivo = 10\n\nSalida: True  # (3 + 7)\n")
print("Ejemplo 3\n")
print("lista = lista = [1, 2, 3]\nobjetivo = 10\n\nSalida: False\n")
print("Restricciones\n- No usar set()\n- No usar itertools\n- No usar funciones avanzadas\n- Solo ciclos," \
" comparaciones y variables auxiliares\n- Puedes usar listas o diccionarios creados por ti")
print("========================================================================")
listaA = [2, 7, 11, 15]
objetivoA = 9

listaB = [3, 5, 1, 7]
objetivoB = 10

listaC = [1, 2, 3]
objetivoC = 10

def sumaParObjetivo(lista, objetivo):
    # for num in lista:
    #     for i in lista[::-1]:
    #         if (i+num) == objetivo:
    #             print("A: ", i, " + B: ", num, " = ", i+num)
    #             print("True")
    #             return
    #         print("A: ", i, " + B: ", num, " = ", i+num)
    # print("False")
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j: 
                print("A:", lista[i], "+ B:", lista[j], "=", lista[i] + lista[j])
                
                if lista[i] + lista[j] == objetivo:
                    print("True")
                    return
    print("False")

sumaParObjetivo(listaA, objetivoA)

print("========================================================================")
