print("========================================================================")
print("Encontrar el elemento que más se repite")
print("Dada una lista de números:\n\nlista = [3, 1, 2, 3, 4, 2, 3, 1, 1, 1, 4]\n")
print("Tu tarea es encontrar cuál es el número que aparece más veces (y cuántas veces aparece).\n")
print("Por ejemplo, la salida esperada sería algo así:\n")
print("El número que más se repite es X y aparece Y veces.\n")
print("Puedes resolverlo usando diccionarios, o intentando no usar diccionarios si quieres más desafío.")

print("========================================================================")

lista = [3, 1, 2, 3, 4, 2, 3, 1, 1, 1, 4]

DiccionarioR = {}

for num in lista:
    if num not in DiccionarioR:
        DiccionarioR[num] = 1
    else:
        DiccionarioR[num] += 1

mas_repite = None
mayor_conteo = 0

for clave in DiccionarioR:
    if DiccionarioR[clave] > mayor_conteo:
        mayor_conteo = DiccionarioR[clave]
        mas_repite = clave
        print("Aqui= ", DiccionarioR[clave], "luego= ", clave)

print("Diccionario de frecuencias:", DiccionarioR)
print(f"El número que más se repite es {mas_repite} y aparece {mayor_conteo} veces.")

print("========================================================================")
