print("========================================================================")
print("Verificar si una lista está ordenada")
print("Dada una lista de números enteros, determina si está ordenada de forma ascendente.")
print("Ejemplo:\n\n[1, 2, 3, 4, 5] → True\n[1, 2, 2, 3]    → True\n[1, 3, 2, 4]    → False\n")
print("Restricciones:\n- No usar sorted()\n- No usar .sort()\n- Solo ciclos, comparaciones y variables auxiliares")
print("========================================================================")
listaA = [1, 2, 3, 4, 5]
listaB = [1, 2, 2, 3]
listaC = [1, 3, 2, 4]

def verificarOrdenAscendente(lista):
    aux = lista[0]

    for num in lista:
        if num >= aux:
            aux = num
        else:
            print("La lista= ", lista, " no esta en ascendente, es FALSE")
            return
    
    print("La lista= ", lista, " si esta en ascendente, es TRUE")
    

verificarOrdenAscendente(listaC)

print("========================================================================")