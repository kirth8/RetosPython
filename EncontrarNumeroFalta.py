print("========================================================================")
print("Encontrar el número faltante")
print("Tienes una lista que contiene números del 1 al n, pero falta exactamente un número.")
print("El orden es aleatorio y no debes usar sorted(), sum(), ni fórmulas matemáticas para series.")
print("Ejemplo:\n")
print("Lista = [3, 1, 5, 2]\n")
print("Aquí falta el 4.\n")
print("Escribe un algoritmo que encuentre qué número falta.\n\nRestricciones:")
print("- No usar sorted()\n- No usar sum()\n- No usar técnicas avanzadas\n- Solo ciclos, comparaciones " \
"y variables auxiliares\n- Puedes recorrer varias veces la lista si es necesario")
print("========================================================================")
lista = [3, 1, 5, 2]

def numeroFaltante(lista):
    auxM = lista[0]
    auxm = lista[0]
    listaC = []

    for num in lista:
        if num > auxM:
            auxM=num
        if num < auxm:
            auxm=num

    for i in range(auxm, auxM+1):
        listaC.append(i)

    for num in listaC:
        if num not in lista:
            print("Este no esta en la lista = ", num)

    print("Auxiliar Mayor: ",auxM, "Auxiliar Menor: ", auxm)        
    print(listaC)


numeroFaltante(lista)

print("========================================================================")