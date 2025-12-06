print("========================================================================")
print("Eliminar duplicados de una lista SIN usar set()")
print("Dada una lista, devuelve otra lista igual pero sin elementos duplicados, manteniendo el " \
"orden original del primero que aparece.")
print("Ejemplo:\n\ninput:  [1, 2, 2, 3, 1, 4, 3]\noutput: [1, 2, 3, 4]\n")
print("Restricciones:\n- No usar set()\n- No usar dict.fromkeys()\n- No usar comprensiones avanzadas")
print("- Solo ciclos, comparaciones y variables auxiliares\n- Puedes crear una nueva lista\n- Mantén el orden original")
print("========================================================================")
lista = [1, 2, 2, 3, 1, 4, 3]
listaR = {}

for num in lista:
    listaR[num] = 1

    
    

print(listaR)
print("========================================================================")