print("========================================================================")
print("Contar cuántos números son mayores que el promedio")
print("Dada una lista de números enteros, debes:")
print("1. Calcular el promedio de la lista")
print("2. Contar cuántos números son mayores que ese promedio")
print("3. Mostrar el resultado")
print("Ejemplo:\n")
print("Lista = [2, 4, 6, 8, 10]\n")
print("Promedio = 6\nNúmeros mayores que 6 → 8 y 10 → 2 números\n")
print("Restricciones:")
print("- No usar sum()")
print("- No usar statistics.mean")
print("- No usar funciones avanzadas")
print("- Solo usar ciclos, comparaciones y variables")
print("- Puedes recorrer la lista varias veces si lo necesitas")
print("========================================================================")
lista = [2, 4, 6, 8, 10]

def contarPromedioMayores(lista):
    Promedio = 0
    aux = 0
    Contador = 0

    for num in lista:   
        Promedio = Promedio + num
        aux += 1

    for num in lista:
        if (Promedio/aux) < num:
            print(num)
            Contador +=1

    print("Se cuentan --> ", Contador)
    print(Promedio, "   /  ", aux, "  --- >  ", Promedio/aux)
contarPromedioMayores(lista)

print("========================================================================")
